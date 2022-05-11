import json
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any, Optional

from pydantic.error_wrappers import ValidationError

from app.domain.entities.error_log import ErrorLog
from app.domain.entities.message_sending_log import MessageSendingLog
from app.domain.entities.message_to_send import MessageToSend
from app.domain.enums.message_sending_status import MessageSendingStatus
from app.repositories.db.base import AbstractDBRepository
from app.repositories.mailer.base import AbstractMailer
from app.repositories.queue.base import AbstractQueueRepository


class AbstractConsumerService(ABC):
	def __init__(self, queue: AbstractQueueRepository, mailer: AbstractMailer, db: AbstractDBRepository):
		self.queue = queue
		self.mailer = mailer
		self.db = db
		self.processed_messages_count = 0

	@abstractmethod
	async def processing_messages(self) -> None:
		"""
		Processing messages from queue.
		"""
		raise NotImplementedError()

	@abstractmethod
	async def _clean_message(self, data: Dict[str, Any]) -> Optional[MessageToSend]:
		raise NotImplementedError()

	@abstractmethod
	async def _save_error_log(self, message: str) -> None:
		raise NotImplementedError()

	@abstractmethod
	async def _send_message_to_email(self, message: MessageToSend) -> None:
		"""
		Send message from queue to email via mailer repository.
		"""
		raise NotImplementedError()


class ConsumerService(AbstractConsumerService):
	async def processing_messages(self) -> None:
		message_gen = self.queue.get_message()

		while True:
			try:
				message = next(message_gen)
			except StopIteration:
				return

			cleaned_message = await self._clean_message(message)

			if cleaned_message is not None:
				await self._send_message_to_email(cleaned_message)
			else:
				await self._save_error_log(json.dumps(message))

			self.processed_messages_count += 1

	async def _save_error_log(self, message: str) -> None:
		error_log = ErrorLog(
			created_at=datetime.now(),
			message=message
		)
		await self.db.save_logs("error_log", error_log)

	async def _clean_message(self, data: Dict[str, Any]) -> Optional[MessageToSend]:
		try:
			return MessageToSend(
				to_email=data.get('to_email'),
				theme=data.get('theme', ''),
				message=data.get('message')
			)
		except ValidationError:
			return None

	async def _send_message_to_email(self, message: MessageToSend) -> None:
		result, err_code, system_message = await self.mailer.send_mail(message)

		if result:
			# the message was sent successfully
			data = MessageSendingLog(
				created_at=datetime.now(),
				status=MessageSendingStatus.SUCCESS,
				sent_from_mail=system_message,
				email=message.to_email,
				theme=message.theme
			)
		else:
			# error when sending the message
			data = MessageSendingLog(
				created_at=datetime.now(),
				status=MessageSendingStatus.FAILED,
				detail=system_message,
				status_code=err_code,
				email=message.to_email,
				theme=message.theme
			)

		await self.db.save_logs("sending_log", data)

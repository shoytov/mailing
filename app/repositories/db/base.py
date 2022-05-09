from abc import ABC, abstractmethod
from typing import Union

from app.domain.entities.error_log import ErrorLog
from app.domain.entities.message_sending_log import MessageSendingLog


class AbstractDBRepository(ABC):
	@abstractmethod
	async def save_logs(self, collection: str, data: Union[ErrorLog, MessageSendingLog]) -> None:
		raise NotImplementedError()

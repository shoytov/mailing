from abc import abstractmethod, ABC
from typing import Any

from app.domain.entities.message_to_send import MessageToSend


class AbstractQueueRepository(ABC):
	consumer: Any

	@abstractmethod
	def __init__(self):
		"""
		It is necessary to define consumer and producer.
		"""
		raise NotImplementedError()

	@abstractmethod
	async def publish_message(self, data: MessageToSend) -> None:
		"""
		Send message to queue.
		"""
		raise NotImplementedError()

	@abstractmethod
	def get_message(self):
		raise NotImplementedError()

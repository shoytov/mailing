from abc import ABC, abstractmethod

from app.domain.entities.message_to_send import MessageToSend
from app.repositories.queue.base import AbstractQueueRepository


class AbstractProducerService(ABC):
	def __init__(self, queue: AbstractQueueRepository):
		self.queue = queue

	@abstractmethod
	async def publish_message(self, data: MessageToSend) -> None:
		"""
		Send message to queue.
		"""
		raise NotImplementedError()


class ProducerService(AbstractProducerService):
	async def publish_message(self, data: MessageToSend) -> None:
		await self.queue.publish_message(data)

from collections import deque

from app.domain.entities.message_to_send import MessageToSend
from .base import AbstractQueueRepository

producer = deque()


class FakeQueue(AbstractQueueRepository):
	"""
	Fake queue for tests.
	"""
	def __init__(self):
		global producer

		self.producer = producer
		self.consumer = self.producer

	async def publish_message(self, data: MessageToSend) -> bool:
		data = data.dict()
		self.consumer.append(data)
		return True

	def get_message(self):
		while self.consumer:
			yield self.consumer.popleft()

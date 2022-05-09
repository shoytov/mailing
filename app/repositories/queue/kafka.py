import asyncio
import json

from aiokafka import AIOKafkaProducer
from kafka import KafkaConsumer

from app.core.settings import (
	KAFKA_HOST,
	KAFKA_PORT,
	KAFKA_TOPIC
)
from app.domain.entities.message_to_send import MessageToSend
from .base import AbstractQueueRepository

loop = asyncio.get_event_loop()


class KafkaRepository(AbstractQueueRepository):
	def __init__(self):
		self.consumer = KafkaConsumer(
			KAFKA_TOPIC,
			bootstrap_servers=[f'{KAFKA_HOST}:{KAFKA_PORT}'],
			enable_auto_commit=False,
			group_id='group1'
		)

		global loop
		self.producer = AIOKafkaProducer(
			loop=loop,
			bootstrap_servers=[f'{KAFKA_HOST}:{KAFKA_PORT}'],
			value_serializer=lambda x: json.dumps(x).encode('utf-8')
		)

	async def publish_message(self, data: MessageToSend) -> None:
		"""
		Send message to queue.
		"""
		data = data.dict()

		await self.producer.start()

		try:
			await self.producer.send(KAFKA_TOPIC, value=data)
		finally:
			await self.producer.stop()

	def get_message(self):
		while True:
			message_batch = self.consumer.poll()

			for partition_batch in message_batch.values():
				for message in partition_batch:
					self.consumer.commit()
					yield json.loads(message.value.decode('utf-8'))

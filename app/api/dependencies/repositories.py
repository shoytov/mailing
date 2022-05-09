from app.repositories.queue.base import AbstractQueueRepository
from app.repositories.queue.kafka import KafkaRepository


def get_queue() -> AbstractQueueRepository:
	return KafkaRepository()

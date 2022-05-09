import asyncio

from app.repositories.db.mongodb_repository import MongodbRepository
from app.repositories.mailer.fastapi_mailer import FastapiMailer
from app.repositories.queue.kafka import KafkaRepository
from app.services.consumer_service import ConsumerService

if __name__ == "__main__":
	loop = asyncio.get_event_loop()

	queue = KafkaRepository()
	mailer = FastapiMailer()
	db = MongodbRepository()

	consumer = ConsumerService(queue, mailer, db)

	loop.run_until_complete(consumer.processing_messages())

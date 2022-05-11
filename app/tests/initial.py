import pytest

from app.repositories.db.fake_db import FakeDb
from app.repositories.mailer.fake_mailer import FakeMailer
from app.repositories.queue.fake_queue import FakeQueue
from app.services.consumer_service import ConsumerService
from app.services.producer_service import ProducerService


@pytest.fixture(scope="package")
def get_producer_service():
	queue = FakeQueue()
	service = ProducerService(queue)

	return service


@pytest.fixture(scope="package")
def get_consumer_service():
	queue = FakeQueue()
	mailer = FakeMailer()
	db = FakeDb()
	service = ConsumerService(queue, mailer, db)

	return service

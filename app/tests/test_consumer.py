import pytest

from app.domain.entities.message_to_send import MessageToSend
from .initial import get_consumer_service, get_producer_service


@pytest.mark.asyncio
class TestConsumer:
	async def test_processed_message(
		self, get_producer_service: get_producer_service,
		get_consumer_service: get_consumer_service
	):
		message = MessageToSend(
			to_email="test_user@mail.ru",
			theme="Test theme",
			message="Message to send"
		)
		await get_producer_service.publish_message(message)

		await get_consumer_service.processing_messages()

		# assert get_consumer_service.processed_messages_count == 1

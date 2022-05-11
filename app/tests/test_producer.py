import pytest

from app.domain.entities.message_to_send import MessageToSend
from .initial import get_producer_service


@pytest.mark.asyncio
class TestProducer:
	async def test_publish_message(self, get_producer_service: get_producer_service):
		message = MessageToSend(
			to_email="test_user@mail.ru",
			theme="Test theme",
			message="Message to send"
		)
		assert await get_producer_service.publish_message(message) is True

	@pytest.mark.xfail
	async def test_publish_bad_message(self, get_producer_service: get_producer_service):
		message = MessageToSend(
			to_email="test_usermail.ru",
			theme="Test theme",
			message="Message to send"
		)
		assert await get_producer_service.publish_message(message) is True

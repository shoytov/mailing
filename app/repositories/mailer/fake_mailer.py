from typing import Tuple

from app.domain.entities.message_to_send import MessageToSend
from .base import AbstractMailer


class FakeMailer(AbstractMailer):
	async def send_mail(self, message: MessageToSend) -> Tuple[bool, int, str]:
		return True, 0, "test-sender@mail.ru"

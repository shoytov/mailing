from abc import ABC, abstractmethod
from typing import Tuple

from app.domain.entities.message_to_send import MessageToSend


class AbstractMailer(ABC):
	@abstractmethod
	async def send_mail(self, message: MessageToSend) -> Tuple[bool, int, str]:
		raise NotImplementedError()

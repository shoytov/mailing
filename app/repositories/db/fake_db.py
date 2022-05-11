from typing import Union

from app.domain.entities.error_log import ErrorLog
from app.domain.entities.message_sending_log import MessageSendingLog
from .base import AbstractDBRepository


class FakeDb(AbstractDBRepository):
	async def save_logs(self, collection: str, data: Union[ErrorLog, MessageSendingLog]) -> None:
		pass

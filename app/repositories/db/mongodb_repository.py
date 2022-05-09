from typing import Union

from motor import motor_asyncio

from app.core.settings import (
	MONGODB_HOST,
	MONGODB_PORT,
	MONGODB_USER,
	MONGODB_PASSWORD,
	MONGODB_DB
)
from app.domain.entities.error_log import ErrorLog
from app.domain.entities.message_sending_log import MessageSendingLog
from .base import AbstractDBRepository


class MongodbRepository(AbstractDBRepository):
	def __init__(self):
		self.client = motor_asyncio.AsyncIOMotorClient(self.connection_string)
		self.db = self.client[MONGODB_DB]

	@property
	def connection_string(self) -> str:
		if MONGODB_USER and MONGODB_PASSWORD:
			_connection_string = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}"
		else:
			_connection_string = f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}"

		return _connection_string

	@connection_string.setter
	def connection_string(self, value: str):
		pass

	async def save_logs(self, collection: str, data: Union[ErrorLog, MessageSendingLog]) -> None:
		collection = self.db[collection]
		await collection.insert_one(data.dict())

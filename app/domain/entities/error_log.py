from datetime import datetime

from pydantic import BaseModel


class ErrorLog(BaseModel):
	"""
	Entity for save bad received message from queue into database.
	"""
	created_at: datetime
	message: str

from enum import Enum


class MessageSendingStatus(str, Enum):
	SUCCESS = "success"
	FAILED = "failed"

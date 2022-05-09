from enum import Enum


class EmailMessageType(str, Enum):
	HTML = 'html'
	PLAIN = 'plain'

from typing import Optional

from pydantic import BaseModel, EmailStr


class MessageToSend(BaseModel):
	to_email: EmailStr
	theme: Optional[str]
	message: str

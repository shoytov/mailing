from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class MessageSendingLog(BaseModel):
	created_at: datetime
	status: str
	sent_from_mail: Optional[EmailStr] = None
	email: EmailStr
	theme: Optional[str] = None
	detail: Optional[str] = None
	status_code: Optional[int] = None

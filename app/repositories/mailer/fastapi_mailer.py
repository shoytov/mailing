from typing import Tuple

from aiosmtplib.errors import SMTPRecipientsRefused, SMTPDataError
from fastapi_mail import FastMail, MessageSchema
from fastapi_mail.errors import ConnectionErrors

from app.core.settings import mail_conf
from app.domain.entities.message_to_send import MessageToSend
from app.domain.enums.email_message_type import EmailMessageType
from .base import AbstractMailer


class FastapiMailer(AbstractMailer):
	def __init__(self):
		self.was_sent = False
		self.err_code = 0
		self.system_message = ""

	async def send_mail(self, message: MessageToSend) -> Tuple[bool, int, str]:
		message = MessageSchema(
			subject=message.theme,
			recipients=[message.to_email],
			body=message.message,
			subtype=EmailMessageType.HTML,
		)

		for mconf in mail_conf:
			fm = FastMail(mconf)

			try:
				await fm.send_message(message)
				self.was_sent = True
				self.system_message = mconf.MAIL_USERNAME
			except ConnectionErrors:
				continue
			except (SMTPRecipientsRefused, SMTPDataError, TypeError) as e:
				if hasattr(e, 'code'):
					if e.code == 451:
						continue

					self.err_code = e.code
					self.system_message = str(e)

		if not self.was_sent and not self.system_message:
			self.system_message = "no one mail account was reached"

		return self.was_sent, self.err_code, self.system_message

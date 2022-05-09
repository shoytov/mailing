"""
Settings for email accounts.
"""

from fastapi_mail import ConnectionConfig
from starlette.config import Config

config = Config(".env")

mail_conf_one = ConnectionConfig(
		MAIL_USERNAME=config.get('MAIL_USERNAME_1'),
		MAIL_PASSWORD=config.get('MAIL_PASSWORD_1'),
		MAIL_FROM=config.get('MAIL_FROM_1'),
		MAIL_PORT=int(config.get('MAIL_PORT_1', default=465)),
		MAIL_SERVER=config.get('MAIL_SERVER_1'),
		MAIL_TLS=False,
		MAIL_SSL=True,
		USE_CREDENTIALS=True
)

mail_conf_two = ConnectionConfig(
		MAIL_USERNAME=config.get('MAIL_USERNAME_2'),
		MAIL_PASSWORD=config.get('MAIL_PASSWORD_2'),
		MAIL_FROM=config.get('MAIL_FROM_2'),
		MAIL_PORT=int(config.get('MAIL_PORT_2', default=465)),
		MAIL_SERVER=config.get('MAIL_SERVER_2'),
		MAIL_TLS=False,
		MAIL_SSL=True,
		USE_CREDENTIALS=True
)

mail_conf = [mail_conf_one, mail_conf_two]

from starlette.config import Config

config = Config(".env")

KAFKA_HOST = config.get("KAFKA_HOST", default="kafka")
KAFKA_PORT = config.get("KAFKA_PORT", default="29092")
KAFKA_TOPIC = config.get("KAFKA_TOPIC", default="mailing")

MONGODB_HOST = config.get("MONGODB_HOST", default="mongo")
MONGODB_USER = config.get("MONGODB_USER", default="testuser")
MONGODB_PASSWORD = config.get("MONGODB_PASSWORD", default="testpass")
MONGODB_PORT = config.get("MONGODB_PORT", default=27017)
MONGODB_DB = config.get("MONGODB_DB", default="mailing")

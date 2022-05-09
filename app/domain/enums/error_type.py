from enum import Enum


class ErrorType(str, Enum):
    """
    List of available error types.
    """
    BUSINESS = "BUSINESS"
    DATABASES = "DATABASES"
    EXTERNAL_CONNECTIONS = "EXTERNAL_CONNECTIONS"
    VALIDATION = "VALIDATION"
    BASE = "BASE"
    MODELS = "MODELS"
    RESOURCE_UNAVAILABLE = "RESOURCE_UNAVAILABLE"

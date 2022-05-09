from fastapi import APIRouter
from .send_message_to_queue import router as send_message_router

router = APIRouter()

router.include_router(send_message_router, prefix="", tags=["v1"])

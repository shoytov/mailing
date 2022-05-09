from typing import Dict

from fastapi import APIRouter, status, Depends

from app.api.dependencies.repositories import get_queue
from app.api.dtos.response_wrapper import ResponseWrapper
from app.domain.entities.message_to_send import MessageToSend
from app.repositories.queue.base import AbstractQueueRepository
from app.services.producer_service import ProducerService

router = APIRouter()


@router.post(
	"/send_message",
	status_code=status.HTTP_201_CREATED,
	response_model=ResponseWrapper[Dict[str, str]],
	operation_id="addMessageToQueue",
	description="Add message to queue"
)
async def send_message(
	data: MessageToSend,
	queue: AbstractQueueRepository = Depends(get_queue)
) -> ResponseWrapper[Dict[str, str]]:
	service = ProducerService(queue)
	await service.publish_message(data)

	return ResponseWrapper[dict].make_success(data={"added": "ok"})

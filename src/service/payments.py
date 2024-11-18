from src.adapters.achilles_processor_adapter import AchillesProcessorAdapter
from src.adapters.base import BaseAdapterT
from src.adapters.midas_processor_adapter import MidasProcessorAdapter
from src.common import (
    AuthorizationRequestDTO,
    AuthorizationResponseDTO,
    ProcessorId,
)

adapters = {
    ProcessorId.ACHILLES: AchillesProcessorAdapter,
    ProcessorId.MIDAS: MidasProcessorAdapter,
}


class PaymentsService:
    def authorize_payment(
        self,
        authorization_request_dto: AuthorizationRequestDTO,
    ) -> AuthorizationResponseDTO:
        adapter: BaseAdapterT = adapters[authorization_request_dto.processor_id]()
        return adapter.authorize_payment(dto=authorization_request_dto)

from src.common import (
    AuthorizationRequestDTO,
    AuthorizationResponseDTO,
    AuthorizationStatus,
)
from src.external.midas_processor import (
    MissingCardDetailsException,
    ThirdPartyMidasProcessor,
)

from .base import BaseAdapter


class MidasProcessorAdapter(BaseAdapter):
    def authorize_payment(
        self, dto: AuthorizationRequestDTO
    ) -> AuthorizationResponseDTO:
        try:
            response: dict = ThirdPartyMidasProcessor().auth(
                amount=dto.amount,
                currency_code=dto.currency_code,
                card_long_number=dto.card_details.card_number,
                security_code=dto.card_details.cvv,
            )
            return AuthorizationResponseDTO(
                processor_transaction_id=response["transaction"]["id"],
                status=AuthorizationStatus.AUTHORIZED
                if response["transaction"]["status"] == "authorised"
                else AuthorizationStatus.DECLINED,
            )
        except MissingCardDetailsException:
            return AuthorizationResponseDTO(
                processor_transaction_id="",
                status=AuthorizationStatus.DECLINED,
            )

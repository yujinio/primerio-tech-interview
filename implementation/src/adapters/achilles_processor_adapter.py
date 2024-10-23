from src.common import (
    AuthorizationRequestDTO,
    AuthorizationResponseDTO,
    AuthorizationStatus,
)
from src.external.achilles_processor import (
    MissingCardDetailsException,
    ThirdPartyAchillesProcessor,
)

from .base import BaseAdapter


class AchillesProcessorAdapter(BaseAdapter):
    def authorize_payment(
        self, dto: AuthorizationRequestDTO
    ) -> AuthorizationResponseDTO:
        try:
            response: dict = ThirdPartyAchillesProcessor().do_authorize(
                card_number=dto.card_details.card_number,
                cvc=dto.card_details.cvv,
                amount=dto.amount,
                currency_code=dto.currency_code,
            )
            return AuthorizationResponseDTO(
                processor_transaction_id=response["achilles_transaction_id"],
                status=AuthorizationStatus.AUTHORIZED
                if response["auth_success"]
                else AuthorizationStatus.DECLINED,
            )

        except MissingCardDetailsException:
            return AuthorizationResponseDTO(
                processor_transaction_id="",
                status="DECLINED",
            )

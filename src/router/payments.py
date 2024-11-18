from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.common import (
    AuthorizationRequestDTO,
    AuthorizationStatus,
    CardDetailsDTO,
    ProcessorId,
)
from src.dependencies import get_payments_service, get_tokenization_service
from src.service.payments import PaymentsService
from src.service.tokenization import TokenizationService

router = APIRouter()


class AuthorizationRequestSchema(BaseModel):
    token: str
    processor_id: ProcessorId
    amount: float
    currency_code: str


class AuthorizationResponseSchema(BaseModel):
    processor_transaction_id: str
    status: AuthorizationStatus


@router.post("/payments", response_model=AuthorizationResponseSchema)
def authorize_payment(
    body: AuthorizationRequestSchema,
    tokenization_service: TokenizationService = Depends(get_tokenization_service),
    payments_service: PaymentsService = Depends(get_payments_service),
) -> AuthorizationResponseSchema:
    card_details = tokenization_service.detokenize(body.token)
    card_details_dto = CardDetailsDTO(
        cardholder_name=card_details.cardholder_name,
        card_number=card_details.card_number,
        cvv=card_details.cvv,
        expiry_year=card_details.expiry_year,
        expiry_month=card_details.expiry_month,
    )
    dto = AuthorizationRequestDTO(
        card_details=card_details_dto,
        processor_id=body.processor_id,
        amount=body.amount,
        currency_code=body.currency_code,
    )
    return payments_service.authorize_payment(dto)

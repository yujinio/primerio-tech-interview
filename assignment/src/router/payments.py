from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.common import AuthorizationStatus, ProcessorId
from src.dependencies import get_tokenization_service
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
) -> AuthorizationResponseSchema:
    raise NotImplementedError

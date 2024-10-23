from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel


class CardDetails(BaseModel):
    cardholder_name: str
    card_number: str
    cvv: str
    expiry_year: str
    expiry_month: str


class AuthorizationStatus(str, Enum):
    AUTHORIZED = "AUTHORIZED"
    DECLINED = "DECLINED"


class ProcessorId(str, Enum):
    ACHILLES = "ACHILLES"
    MIDAS = "MIDAS"


@dataclass(frozen=True)
class CardDetailsDTO:
    cardholder_name: str
    card_number: str
    cvv: str
    expiry_year: str
    expiry_month: str


@dataclass(frozen=True)
class AuthorizationRequestDTO:
    card_details: CardDetailsDTO
    processor_id: ProcessorId
    amount: float
    currency_code: str


@dataclass(frozen=True)
class AuthorizationResponseDTO:
    processor_transaction_id: str
    status: AuthorizationStatus

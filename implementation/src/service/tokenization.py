import uuid
from typing import Optional

from src.common import CardDetails


class TokenizationService:
    def __init__(self) -> None:
        self.store: dict[str, CardDetails] = {}

    def tokenize(
        self,
        cardholder_name: str,
        card_number: str,
        cvv: str,
        expiry_year: str,
        expiry_month: str,
    ) -> str:
        id_ = str(uuid.uuid4())
        self.store[id_] = CardDetails(
            cardholder_name=cardholder_name,
            card_number=card_number,
            cvv=cvv,
            expiry_year=expiry_year,
            expiry_month=expiry_month,
        )
        return id_

    def detokenize(self, token: str) -> Optional[CardDetails]:
        return self.store.get(token)

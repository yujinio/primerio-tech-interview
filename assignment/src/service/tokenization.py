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
        raise NotImplementedError

    def detokenize(self, token: str) -> Optional[CardDetails]:
        return self.store.get(token)

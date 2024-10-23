from abc import ABC, abstractmethod
from typing import TypeVar

from src.common import AuthorizationRequestDTO, AuthorizationResponseDTO


class BaseAdapter(ABC):
    @abstractmethod
    def authorize_payment(
        self, authorization_request_dto: AuthorizationRequestDTO
    ) -> AuthorizationResponseDTO:
        raise NotImplementedError


BaseAdapterT = TypeVar("BaseAdapterT", bound=BaseAdapter)

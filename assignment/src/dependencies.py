from starlette.requests import Request

from src.service.tokenization import TokenizationService


async def get_tokenization_service(request: Request) -> TokenizationService:
    # The tokenization service is a stateful service, so we need to make sure that we only create one instance of it
    try:
        service: TokenizationService = request.app.state.tokenization_service
    except AttributeError:
        service = TokenizationService()
        request.app.state.tokenization_service = service
    return service

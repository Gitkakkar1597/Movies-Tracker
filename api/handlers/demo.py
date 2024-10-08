from fastapi import APIRouter

from api.responses.detail import DetailResponse

router = APIRouter(prefix="/api/v1/demo")


@router.get("/", response_model=DetailResponse)
def hello_world():
    # hello endpoint
    return DetailResponse(message="Hello!")

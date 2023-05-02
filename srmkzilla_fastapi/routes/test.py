from fastapi import APIRouter, Response
from json import dumps

router = APIRouter(
    prefix="/test",
)

@router.get("/")
async def test():
    return Response(
        dumps({"message": "Nothing to see here"}),
        status_code=200,
        media_type="application/json"
    )
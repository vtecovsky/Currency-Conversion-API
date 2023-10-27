from fastapi import HTTPException
from starlette import status


class CurrencyNotFound(HTTPException):
    """
    HTTP_400_BAD_REQUEST
    """

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No such currency",
        )

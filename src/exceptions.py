from fastapi import HTTPException
from starlette import status


class CurrencyNotFound(HTTPException):
    """
    HTTP_404_NOT_FOUND
    """

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such currency",
        )


class NoLastUpdate(HTTPException):
    """
    HTTP_404_NOT_FOUND
    """

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There hasn't been an update yet",
        )

from fastapi import HTTPException
from starlette import status


class CollisionInBookings(HTTPException):
    """
    HTTP_409_CONFLICT
    """

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="detail",
        )
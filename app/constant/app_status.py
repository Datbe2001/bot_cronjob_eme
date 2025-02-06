from enum import Enum

from starlette import status


class AppStatus(Enum):
    SUCCESS = status.HTTP_200_OK, "200", 'SUCCESS'

    ERROR_BAD_REQUEST = status.HTTP_400_BAD_REQUEST, "400", 'BAD_REQUEST'

    ERROR_UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED, "401", 'UNAUTHORIZED'

    ERROR_404_NOT_FOUND = status.HTTP_404_NOT_FOUND, "404", 'NOT_FOUND'

    ERROR_METHOD_NOT_ALLOWED = status.HTTP_405_METHOD_NOT_ALLOWED, "405", 'METHOD_NOT_ALLOWED'

    ERROR_CONFLICT = status.HTTP_409_CONFLICT, "409", 'CONFLICT'

    ERROR_INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR, "500", 'INTERNAL_SERVER_ERROR'

    @property
    def status_code(self):
        return self.value[0]

    @property
    def app_status_code(self):
        return self.value[1]

    @property
    def message(self):
        return self.value[2]

    @property
    def meta(self) -> dict:
        return dict(status_code=self.value[0], detail=self.value[2])

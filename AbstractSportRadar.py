import abc
from typing import Final

class AbstractSportRadar(abc.ABC):
    BASE_URL: Final = "http://api.sportradar.us"
import abc
from typing import Final
from AbstractSportRadar import AbstractSportRadar


class AbstractNcaamb(AbstractSportRadar, metaclass=abc.ABC):
    SPORT_URL: Final = "/ncaamb/trial/v7/en/"
    EXTENDED_URL: Final = super().BASE_URL + SPORT_URL
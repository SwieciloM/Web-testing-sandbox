from enum import Enum


class ParkingType(Enum):
    VALET = "valet"
    SHORT_TERM = "short_term"
    LONG_TERM_GARAGE = "long_term_garage"
    LONG_TERM_SURFACE = "long_term_surface"
    ECONOMY = "economy"

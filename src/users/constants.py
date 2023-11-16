from enum import StrEnum, auto
from functools import lru_cache


class Status(StrEnum):
    OPENED = auto()
    ASSIGNED = auto()
    CLOSED = auto()


class Role(StrEnum):
    ADMIN = "AD"
    SENIOR = "SR"
    JUNIOR = "JR"

    @classmethod
    @lru_cache(maxsize=1)
    def choices(cls) -> list[tuple[str, str]]:
        # ['SR', 'JR']
        # [item for item in Role]
        results = []

        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results

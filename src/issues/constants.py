from functools import lru_cache
from enum import StrEnum, auto


class Status(StrEnum):
    OPENED = auto()  
    ASSIGNED = auto()  
    CLOSED = auto()  

    @classmethod
    @lru_cache(maxsize=1)
    def choices(cls) -> list[tuple[str, str]]:
        results = []
        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results

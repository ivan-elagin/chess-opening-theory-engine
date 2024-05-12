""" This module contains the colours and aliases used in the program. """

from typing import Self
from enum import StrEnum

Square = tuple[int, int]


class Colour(StrEnum):
    """Enum class for piece colours."""
    WHITE = "white"
    BLACK = "black"

    def __invert__(self) -> Self:
        return Colour.BLACK if self == Colour.WHITE else Colour.WHITE

    def __str__(self) -> str:
        return self.value.title()
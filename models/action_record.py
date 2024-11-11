"""
Represents an action record for every user in everyday.
"""

__author__ = "LUOYAN WEI"

from dataclasses import dataclass

@dataclass
class ActionRecord:
    day: int
    exercise: str
    diet: str
    duration: float
    calories_burned: float = 0.0
    total_calories_burned: float = 0.0
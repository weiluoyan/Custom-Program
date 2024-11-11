"""
Represents the daily progress of a user.
"""

__author__ = "LUOYAN WEI"

from dataclasses import dataclass
@dataclass
class DailyProgress:
    day: int
    exercises: list
    diet: str
    total_calories_burned: float = 0.0
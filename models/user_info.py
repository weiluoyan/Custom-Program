"""
Represents the basic information of a user.
"""

__author__ = "LUOYAN WEI"

from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    age: int
    weight: float
    height: float
    target_weight: float
    classified: str
    avg_daily_calories: float
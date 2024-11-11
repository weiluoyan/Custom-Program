"""
Provides functionality for displaying messages, inculding welcome_message, motivational prompts and certification for users when theny finished the fitness journey.
"""

__author__ = "LUOYAN WEI"

import random
from models.user_info import UserInfo

motivational_messages = [
    "Great job today! Remember: consistency is key!",
    "Fantastic effort today! Keep pushing toward your goal!",
    "You're doing amazing! One day closer to your dream!",
    "Excellent work today! Every effort counts!",
    "Superb! Keep up the good work, and you'll see the results!"
]

def welcome_message():
    """
    display welcome messages
    """
    welcome_message = """
*******************************************************
*                                                     *
*🎉🎉🎉Welcome to "I Have a Dream in Lose Weight"🎉🎉🎉 *
*                                                     *
*                💪 Stay Strong! 💪                    *
*                                                     *
*******************************************************
"""
    print(welcome_message)
    
    
def random_motivational_message() -> str:
    """
    display motivational message
    """
    return random.choice(motivational_messages)


def generate_certificate(user: UserInfo, day_needed: int) -> str:
    """ 
    display the Certification
    """
    return (
        f"🎖️ Certificate of Achievement 🎖️\n"
        f"Congratulations {user.name}! You've successfully completed the {day_needed}-day challenge.\n"
        f"Your commitment to becoming a better version of yourself is truly inspiring!\n"
        f"Final Weight: {user.weight:.2f} kg\n"
    )
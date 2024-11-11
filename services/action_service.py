"""
Handles daily user activity, including exercise, diet tracking, and progress monitoring.
"""

__author__ = "LUOYAN WEI"

from models.daily_progress import DailyProgress
from models.user_info import UserInfo
from services.level_service import random_motivational_message
import time
from enum import Enum

class ExerciseType(Enum):
    CARDIO = 8
    STRENGTH_TRAINING = 6
    YOGA = 4
    RUNNING = 10
    CYCLING = 7
    SWIMMING = 9
    JUMP_ROPE = 12
    HIIT = 11
    WALKING = 3
    FOOTY = 10
    SQUASH = 15
    BOXING = 30
    BIKE_POLO = 45
    WATER_POLO = 50


class DietType(Enum):
    DIET_211 = "211 Diet: 2 servings of vegetables, 1 serving of protein, 1 serving of carbs"
    LOW_CARB = "Low Carb Diet: Limited carbs, higher fat and protein intake"
    HIGH_PROTEIN = "High Protein Diet: Focus on protein for muscle maintenance and fat loss"
    VEGETARIAN = "Vegetarian Diet: Plant-based diet with balanced nutrients"
    BALANCED = "Balanced Diet: Equal portions of carbs, fats, and proteins"



def read_an_int(query: str) -> int:
    """Support input a int number and check the vaild."""
    value: int = None # value obtained from the user 
    while value is None:
        try:
            value = int(input(f"{query}: "))
        except ValueError:
            print("Invalid input number. Please enter a valid number.")
    return value



def read_an_float(query: str) -> float:
    """Support input a float number and check the vaild."""
    value: float= None # value obtained from the user 
    while value is None:
        try:
            value = float(input(f"{query}: "))
        except ValueError:
            print("Invalid input number. Please enter a valid number.")
    return value



def display_log(progress_log: list):
    """
    Display the historical log of user's process
    """
    if not progress_log:
        print("\n🗒️ No progress log available yet.") 
    else:
        print("\n📊 Progress Log 📊")
        print("---------------------------------------------------")
        for entry in progress_log:
            print(f"Day {entry['day']}:")
            print(f" - Exercises: {', '.join([f'{ex[0]} for {ex[1]} hrs' for ex in entry['exercises']])}")
            print(f" - Total Calories Burned: {entry['calories_burned']:.2f}")
            print(f" - Diet: {entry['diet']}")
            print(f" - Weight: {entry['weight']:.2f} kg")
            print("---------------------------------------------------")
 


def estimate_exercise_hours(calorie_goal: float, weight: float):
    """
    Estimate how many hours of each exercise are needed to reach the calorie burn goal
    """
    exercise_plan = []
    print("\n🔍 Based on your calorie goal, here's an estimate of how many hours you need for each exercise:\n")
    for exercise in ExerciseType:
        hours_needed = calorie_goal / (exercise.value * weight)
        exercise_plan.append((exercise.name.replace('_', ' ').title(), round(hours_needed, 2)))  # Round to 2 decimal places
        print(f" - {exercise.name.replace('_', ' ').title()}: {round(hours_needed, 2)} hours")
    


def record_daily_action(day: int, weight: float) -> DailyProgress:
    """
    Record daily exercise and diet  
    """ 
    print(f"\n--- Day {day} Activity ---\n")
    print("\n💪 The First Step: Choose Your Exercise 💪")
    print("---------------------------------------------------")

    exercises = []
    total_calories_burned = 0.0
    add_more: str

    # Loop to allow the user to select multiple exercises
    add_more = "y"
    while add_more == "y":
        # Display exercise options
        print("Choose from the following exercises and their burn rates:\n")

        for idx, exercise in enumerate(ExerciseType, 1):
            print(f"{idx}. {exercise.name.replace('_', ' ').title()}")
            print(f"   Burn rate: {exercise.value} cal/kg/hr")
            print("---------------------------------------------------")

        # Get exercise choice
        exercise_choice = read_an_int(f"\nChoose an exercise for day {day} (1-{len(ExerciseType)}): ")
        selected_exercise = list(ExerciseType)[exercise_choice - 1]
        duration = read_an_float(f"How long did you do {selected_exercise.name.replace('_', ' ').title()} today (in hours)? ")
        exercises.append((selected_exercise.name.replace('_', ' ').title(), duration))

        # Calculate calories burned for this exercise
        calories_burned = selected_exercise.value * weight * duration
        total_calories_burned += calories_burned

        # Ask if user wants to add more exercises
        value_input = True
        while value_input:
            add_more = input("Do you want to add another exercise? (y/n): ").lower()
            if add_more in ["y", "n"]:
                value_input = False
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        if add_more == "n":
            break
 
        

    # Display diet options
    print("\n🥗 The Second Step: Choose Your Diet 🥗")
    print("---------------------------------------------------")
    print("Choose from the following diet plans:\n")

    for idx, diet in enumerate(DietType, 1):
        print(f"{idx}. {diet.value}")
        print("---------------------------------------------------")

    diet_choice = read_an_int(f"Choose your diet for day {day} (1-{len(DietType)}): ")
    selected_diet = list(DietType)[diet_choice - 1]

    return DailyProgress(day, exercises, selected_diet.value, total_calories_burned)


def calculate_daily_calories(progress: DailyProgress, weight: float) -> float:
    """
    Calculate total calories burned from all exercises for the day.
    Takes into account the user's weight and the burn rate of each exercise.
    """
    total_calories = 0
    for exercise, duration in progress.exercises:
        burn_rate = ExerciseType[exercise.upper().replace(" ", "_")].value
        total_calories += burn_rate * weight * duration
    
    return total_calories 


def track_progress(user: UserInfo, days_needed):
    """
    Track daily progress with motivational messages and detailed information.
    Handles both weight loss and weight gain scenarios.
    """
    progress_log = []

    for day in range(1, days_needed + 1):
        print(f"\n--- Day {day} of {days_needed} ---")
        print(f"🎯 You have {days_needed - day} days left. Stay focused and keep it up!\n")

        # Record the user's daily exercise and diet actions
        daily_progress = record_daily_action(day, user.weight)
        daily_calories = calculate_daily_calories(daily_progress, user.weight)

        # Check if the user is trying to lose or gain weight
        if user.weight > user.target_weight:
            # Weight loss logic
            print(f"\n🔥 You burned {daily_calories:.2f} calories today!")
            weight_loss = daily_calories / 7700  # 7700 calories ≈ 1 kg weight loss
            user.weight -= weight_loss  # Decrease weight for weight loss

            # Display progress and updated weight for weight loss
            print("\n🔄 Updating your progress...")
            time.sleep(1) 
            print(f"💪 Your current weight is now: {user.weight:.2f} kg! You lost {weight_loss:.2f} kg today!")

        else:
            # Weight gain logic
            print(f"\n🍽️ You consumed {daily_calories:.2f} calories today!")
            weight_gain = daily_calories / 7700  # 7700 calories ≈ 1 kg weight gain
            user.weight += weight_gain  # Increase weight for weight gain

            # Display progress and updated weight for weight gain
            print("\n🔄 Updating your progress...")
            time.sleep(1) 
            print(f"💪 Your current weight is now: {user.weight:.2f} kg! You gained {weight_gain:.2f} kg today!")
        
        # Log the day's progress
        progress_log.append({
            'day' : day,
            'exercises' : daily_progress.exercises,
            'calories_burned' : daily_calories,
            'diet' : daily_progress.diet,
            'weight' : user.weight
        })
        
        action_valid = False
        while not action_valid:
            next_action = input("\nWould you like to (v)iew the log or (p)roceed to the next day? (v/p): ").lower()
            if next_action == 'v':
                display_log(progress_log)
                input("\nPress Enter to continue to the next day...")
                action_valid = True
            elif next_action == 'p':
                action_valid = True
            else:
                print("Invalid input. Please enter 'v' to view the log or 'p' to proceed.")


        # Show motivational message
        print(f"\n💬 {user.name}, " + random_motivational_message())

        # Show a reminder of the number of days completed and remaining
        print(f"📅 You have completed {day} day(s) and have {days_needed - day} day(s) left.\n")


        # Check if the target weight has been reached for both loss and gain scenarios
        if user.weight <= user.target_weight and user.weight > user.target_weight:
            print(f"🎉 Congratulations! You've reached your target weight of {user.target_weight:.2f} kg!")
            break
        elif user.weight >= user.target_weight and user.weight < user.target_weight:
            print(f"🎉 Congratulations! You've reached your target weight of {user.target_weight:.2f} kg!")
            break

    # If the user finishes all days without reaching the target weight
    if user.weight > user.target_weight:
        print(f"💪 Great job completing {days_needed} days! Keep going to reach your final goal!")
    elif user.weight < user.target_weight:
        print(f"💪 Great job completing {days_needed} days! Keep working to reach your final goal!")

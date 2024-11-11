"""
Provides functionality for gathering user userinfomation, calculate user's BMI and measure user's day which they needed in this fitness journey.
"""

__author__ = "LUOYAN WEI"

from models.user_info import UserInfo


def get_user_info() -> UserInfo:
    """
    Get user's data including name, weight, height, and target weight, and calculate BMI.
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    # Validate weight input
    weight_valid = False
    while not weight_valid:
        try:
            weight = float(input("Enter your weight (kg): "))
            weight_valid = True
        except ValueError:
            print("Invalid input for weight. Please enter a valid number.")

    # Validate height input
    height_valid = False
    while not height_valid:
        try:
            # Replace any comma in the height input with a decimal point
            height_input = input("Enter your height (m): ").replace(',', '.')
            height = float(height_input)
            height_valid = True
        except ValueError:
            print("Invalid input for height. Please enter a valid number (e.g., 1.75).")

    # Validate target weight input
    target_weight_valid = False
    while not target_weight_valid:
        try:
            target_weight = float(input("Enter your target weight (kg): "))
            if target_weight > weight:
                print("It looks like you want to build muscle. Let's do it.")
            target_weight_valid = True
        except ValueError:
            print("Invalid input for target weight. Please enter a valid number.")

    avg_daily_calories = float(input("Enter the average calories you plan to burn daily (e.g., 1000): "))
    
    # Calculate BMI
    classified = calculate_bmi(weight, height)
    
    # Create and return a UserInfo object
    return UserInfo(name, age, weight, height, target_weight, classified, avg_daily_calories)


def calculate_bmi(weight, height) -> str:
    """
    Calculate user's bmi
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        return "Thin!"
    elif 18.5 <= bmi < 24.9:
        return "Normal!"
    else:
        return "Overweight!"


def estimate_days(weight: float, target_weight: float, daily_calories: float) -> int:
    """
    Estimate how many days are needed based on daily calorie burn 
    Handles both weight lose(when weight > target_weight) or weight gain(when weight < target_weight)
    """
    weight_different = target_weight - weight
    if weight_different > 0:
        total_calories_needed = weight_different * 7700
        day_needed = int(total_calories_needed // daily_calories)
        return max(day_needed, 0)
    else:
        weight_loss_needed = weight - target_weight
        total_calories_needed = weight_loss_needed * 7700  # 1 kg = 7700 calories
        day_needed = int(total_calories_needed // daily_calories)
        return max(day_needed, 0)
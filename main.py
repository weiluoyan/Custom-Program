"""
Main program for the "I have a dream in lose weight" fitness journey. 
This script guides uses through setting up a personalized fitness plan, tracking daily progress, and ultimately generating a certificate of achievement
"""

__author__ = "LUOYAN WEI"

from services.user_service import get_user_info, estimate_days
from services.action_service import estimate_exercise_hours
from services.level_service import generate_certificate, welcome_message
from services.action_service import track_progress

def main():
    # Celebratory message with stars and decorations
    welcome_message() 
    
    # Get user information and aim
    user = get_user_info()

    # Initialize change_plan flag
    change_plan = "y"
    # Loop for recalculating days_needed until the user is satisfied
    while change_plan == "y":
        # Estimate how many days it will take to reach the goal
        days_needed = estimate_days(user.weight, user.target_weight, user.avg_daily_calories)
        
        print("📋 Your Action Plan:")
        print(f"\nYou are currently classified as {user.classified} based on your BMI.\n")
        print(f"\nTo reach your target weight of {user.target_weight} kg, you'll need approximately {days_needed} days.\n")
       
        # Provide an estimate of how many hours are needed
        estimate_exercise_hours(user.avg_daily_calories, user.weight)
        
        # Check if the user wants to change the plan
        change_plan = input("\nDo you want to change your average calories to burn daily (y/n): ").lower()
        if change_plan == "y":
            user.avg_daily_calories = float(input("Enter the new average calories you plan to burn daily (e.g., 1000): "))
        elif days_needed == 0:
            print("\nKeep going! You don't need to do any exercise!")
            break
        else:
            print("\nThe plan looks good! Let's get started.")
            break   
    
    # Game Loop: start tracking daily progress
    if days_needed > 0: 
        track_progress(user, days_needed)
     
    # Completion of days_needed Days
    print("\n🎉🎉🎉 Congratulations! 🎉🎉🎉")
    print(generate_certificate(user, days_needed))
    print("Thank you for joining 'I Have a Dream in Lose Weight'. Keep striving to be the best version of yourself!")

if __name__ == "__main__":
    main()
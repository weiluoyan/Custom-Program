# Custom Program

The Better Me program is a Python-based application designed to help users set realistic fitness goals based on their current weight and height. By calculating the estimated days needed to reach their desired weight, the program provides a structured, gamified approach to tracking progress, offering exercise ideas, diet options, and motivation throughout the journey.

Features

	•	Personalized Day Calculation: Estimates the number of days needed to reach the target weight based on the user’s weight, height, and BMI.
	•	Exercise and Diet Tracking: Users can log daily exercises and select from various diet options tailored to their goals.
	•	Calories and Progress Tracking: Tracks calories burned based on the exercises performed and updates weight accordingly.
	•	Gamified Experience: The program offers points, progress feedback, and a motivational community feature to keep users engaged.
	•	Daily Progress Log: Logs each day’s activities, including exercises, calories burned, and updated weight, helping users track their journey toward their goals.

## Project Structure

The project is organized as follows:
Custom Program/
├── models/
│   ├── action_record.py        # Defines models and functions for action records
│   ├── daily_progress.py       # Handles daily progress tracking
│   └── user_info.py            # Manages user information models
├── services/
│   ├── action_service.py       # Service functions related to actions
│   ├── level_service.py        # Service functions related to user levels
│   └── user_service.py         # Service functions related to user data management
├── main.py                     # Main entry point of the program
└── README.md                   # Project documentation

### Files Overview

- **models/**: This folder contains data models that define the structure of user information, action records, and daily progress.
  - `action_record.py`: Manages records of user actions.
  - `daily_progress.py`: Tracks user progress on a daily basis.
  - `user_info.py`: Contains user information and profile details.

- **services/**: This folder contains service modules for handling business logic and interactions between models.
  - `action_service.py`: Provides functionalities for managing actions.
  - `level_service.py`: Manages user levels and related functionalities.
  - `user_service.py`: Handles interactions related to user data.

- **main.py**: The main script to initialize and run the program.

### Requirements

Ensure you have Python 3.6+ installed. Install any necessary dependencies if specified in the future.

### Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Custom-Program.git
   cd Custom-Program

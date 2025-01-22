# **Python Personal Fitness Tracker System**
 Welcome to my project! This Python project implements *conditional statements*, *loops*, *lists*, *functions* and varying user *inputs* in order to create a unique **Personal Fitness Tracker System**.

## Project Overview:
This project focuses on using **Python basics** like strings, lists, loops, conditionals, and functions. 

## Objectives:
The goal of this project is to create a fitness tracker system that enables users to:  
- Log workouts and calorie intake.   
- Track their daily progress.  
- Reset daily progress and receive motivational feedback.

## User instructions:
1. **Log Workout**  
   Allows users to log the type of workout and duration (e.g., "Running" for 30 minutes).  

2. **Log Calorie Intake**  
   Allows users to log calorie intake for meals.  

3. **View Progress**  
   Displays the total workout time and calorie intake for the day with motivational feedback.  

4. **Reset Progress**  
   Clears all workout and calorie data for the day.  

5. **Set Daily Goals**  
   Allows users to set goals for daily workout duration and calorie intake.  

6. **Encouragement System**  
   Provides feedback based on whether the daily goals are met.

---

## Python Code:
Below is the code with comments that guide through the project activities.
```python
workouts = []
calories = []

workout_goal = 0
calorie_goal = 0

def log_workout():  # Function that inputs workout type and duration.
    workout_type = input('Workout type: ')
    duration = int(input('Workout duration: '))
    workouts.append(duration)
    print(f'Successfully saved {workout_type} data! \n')

def log_calorie_intake():  # Function that inputs calorie intake.
    calories_consumed = int(input('Calories consumed: '))
    calories.append(calories_consumed)
    print(f'Successfully consumed {calories_consumed} calories! \n')

def view_progress():  # Function that tracks the daily progress.
    print('*** Daily progress ***')
    print(f'Total workout time: {sum(workouts)}')
    print(f'Total calories: {sum(calories)}')
    encouragement_system()

def reset_progress():  # Function that resets the daily progress. 
    workouts.clear()
    calories.clear()
    print('Successfully reset progress on workouts and calorie intake! \n')


def set_daily_goals():  # Function that lets the user set individual daily goals. 
    global workout_goal, calorie_goal
    workout_goal = int(input('Input daily workout goal in minutes: '))
    calorie_goal = int(input('Input daily calorie intake goal: '))
    print('Goals successfully set! \n')

def encouragement_system():  # Functions that determines the type of message that is shown. 
    if sum(workouts) == 0 and sum(calories) == 0:
        print('No workout or calorie intake data. \n')
    else:
        if sum(workouts) >= workout_goal:
            print('Achieved workout goal! You rock! ')
        else:
            print(f'Don\'t give up! Only {workout_goal - sum(workouts)} '
                  f'more minutes of workout until you reach your goal! ')

        if sum(calories) >= calorie_goal:
            print('Achieved calorie intake goal! Keep it up! \n')
        else:
            print(f'You\'re so close! Only {calorie_goal - sum(calories)} '
                  f'more calories until you reach your intake goal! \n')

def main():
    print("Welcome to the Personal Fitness Tracker System \n")

    # Display menu options
    while True: 
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':    # Prompt for workout type and duration
            log_workout()
        elif choice == '2':  # Prompt for calories consumed
            log_calorie_intake()
        elif choice == '3':  # Call view_progress function
            view_progress()
        elif choice == '4':  # Call reset_progress function
            reset_progress()
        elif choice == '5':  # Prompt for daily goals
            set_daily_goals()
        elif choice == '6':  # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! ")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
```

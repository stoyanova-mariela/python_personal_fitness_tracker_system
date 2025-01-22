workouts = []
calories = []

workout_goal = 0
calorie_goal = 0

def log_workout():
    workout_type = input('Workout type: ')
    duration = int(input('Workout duration: '))
    workouts.append(duration)
    print(f'Successfully saved {workout_type} data! \n')

def log_calorie_intake():
    calories_consumed = int(input('Calories consumed: '))
    calories.append(calories_consumed)
    print(f'Successfully consumed {calories_consumed} calories! \n')

def view_progress():
    print('*** Daily progress ***')
    print(f'Total workout time: {sum(workouts)}')
    print(f'Total calories: {sum(calories)}')
    encouragement_system()

def reset_progress():
    workouts.clear()
    calories.clear()
    print('Successfully reset progress on workouts and calorie intake! \n')


def set_daily_goals():
    global workout_goal, calorie_goal
    workout_goal = int(input('Input daily workout goal in minutes: '))
    calorie_goal = int(input('Input daily calorie intake goal: '))
    print('Goals successfully set! \n')

def encouragement_system():
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

    while True:
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            log_workout()
        elif choice == '2':
            log_calorie_intake()
        elif choice == '3':
            view_progress()
        elif choice == '4':
            reset_progress()
        elif choice == '5':
            set_daily_goals()
        elif choice == '6':
            print("Thank you for using the Fitness Tracker. Stay healthy! ")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
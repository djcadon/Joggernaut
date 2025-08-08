from db_config import connect_db

print("""
            Welcome to the CLI for the Fitness Tracker App
      *************************************************************
          _  ___   ____  ____ _____ ____  _   _    _   _   _ _____ 
         | |/ _ \ / ___|/ ___| ____|  _ \| \ | |  / \ | | | |_   _|
      _  | | | | | |  _| |  _|  _| | |_) |  \| | / _ \| | | | | |  
     | |_| | |_| | |_| | |_| | |___|  _ <| |\  |/ ___ \ |_| | | |  
      \___/ \___/ \____|\____|_____|_| \_\_| \_/_/   \_\___/  |_|
      *************************************************************

     """)

print("Available Tables:\n")
#Dictionary to map table numbers to names
tables = {  
            1:"Users",
            2:"User Metrics",
            3:"Friends",
            4:"Workouts",
            5:"Exercises",
            6:"Exercise_Workout",
            7:"Progress",
            8:"Goals"
         }
#Display available tables
for key, value in enumerate(tables.items(), start=1):
    print(f"{key}. {value[1]}")
print("\nEnter which table you want to interact with or 'exit' to quit:")
#Function to handle user input for table selection
def handle_tables():
    while True:
        user_input = input().strip().lower()
        match user_input:
            #Users table
            case "1":
               print("You selected Users table.")
               return 1
            #User Metrics table
            case "2":
                print("You selected User Metrics table.")
                return 2
            #Friends table
            case "3":
                print("You selected Friends table.")
                return 3
            #Workouts table
            case "4":
                print("You selected Workouts table.")
                return 4
            #Exercises table
            case "5":
                print("You selected Exercises table.")
                return 5
            #Exercise_Workout table
            case "6":
                print("You selected Workout_Exercises table.")
                return 6
            #Progress table
            case "7":
                print("You selected Progress table.")
                return 7
            #Goals table
            case "8":
                print("You selected Goals table.")
                return 8
            #Exit the CLI
            case 'exit':
                print("Exiting the CLI. Goodbye!")
                exit(0)
            #Invalid input
            case _:
                print("Invalid input. Please try again.")
selected_table = handle_tables()
#Dictionary to map operations for each table
operations = {  
                "Users":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["Name", "Password", "Date Of Birth"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "User Metrics":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["Weight", "Height"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Friends":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["FriendID", "UserID"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Workouts":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["Name", "DaysOfTheWeek"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Exercises":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["Name", "Description"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Exercise_Workout":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["WorkoutID", "ExerciseID"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Progress":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["UserID", "ExerciseID", "WorkoutID", "Weight", "DurationMins"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Goals":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":["UserID", "GoalWeight"],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
             }
#Function to handle user input for operation selection
def handle_operations(selected_table):
    table_name = tables[selected_table]
    print(f"Available operations for {table_name} table:")
    for key, value in enumerate(operations[table_name].keys(), start=1):
        print(f"{key}. {value}")
    print("\nEnter which operation you want to perform or 'exit' to quit:")

    while True:
        user_input = input().strip().lower()
        match user_input:
            case "0":
                print("You selected the main menu. Returning to table selection.")
                return handle_tables()

            case "1":
                        print("Choose a SELECT option:")
                        print("1. SELECT *")
                        print("2. SELECT BY ID")
                        select_choice = input("Enter choice (1 or 2): ").strip()
                        
                        if select_choice == "1":
                            select_all_users()
                        elif select_choice == "2":
                            select_user_by_id()
                        else:
                            print("Invalid option.")


            case "2":
                insert_user()

            case "3":
               update_user_by_id()
            case "4":
              delete_user_by_id()
                
            case 'exit':
                print("Exiting the CLI. Goodbye!")
                exit(0)

            case _:
                print("Invalid input. Please try again.")

handle_operations(selected_table)

# Mock operation functions
def select_all_users():
    print("SELECT * FROM Users")
    print("(1, 'Alex', 'secret123', '2000-01-01')")
    print("(2, 'Jamie', 'pass456', '1999-12-31')")

def select_user_by_id():
    user_id = input("Enter user ID to view: ")
    print(f"SELECT * FROM Users WHERE UserID = {user_id}")
    print(f"(Mocked) User ID {user_id}: ('Alex', 'secret123', '2000-01-01')")

def insert_user():
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    print(f"INSERT INTO Users (Name, Password, DateOfBirth) VALUES ('{name}', '{password}', '{dob}')")
    print("User inserted successfully (mock).")

def update_user_by_id():
    user_id = input("Enter ID of the user to update: ")
    name = input("Enter new Name: ")
    password = input("Enter new Password: ")
    dob = input("Enter new Date of Birth (YYYY-MM-DD): ")
    print(f"UPDATE Users SET Name = '{name}', Password = '{password}', DateOfBirth = '{dob}' WHERE UserID = {user_id}")
    print("User updated successfully (mock).")

def delete_user_by_id():
    user_id = input("Enter ID of the user to delete: ")
    print(f"DELETE FROM Users WHERE UserID = {user_id}")
    print("User deleted successfully (mock).")


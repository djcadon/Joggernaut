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

print("Available Tables:")
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
print("Enter which table you want to interact with or 'exit' to quit:")
#Function to handle user input for table selection
def handle_tables():
    while True:
        user_input = input().strip().lower()
        match user_input:
            case 1:
               print("You selected Users table.")
               return 1
            case 2:
                print("You selected User Metrics table.")
                return 2
            case 3:
                print("You selected Friends table.")
                return 3
            case 4:
                print("You selected Workouts table.")
                return 4
            case 5:
                print("You selected Exercises table.")
                return 5
            case 6:
                print("You selected Workout_Exercises table.")
                return 6
            case 7:
                print("You selected Progress table.")
                return 7
            case 8:
                print("You selected Goals table.")
                return 8
            case 'exit':
                print("Exiting the CLI. Goodbye!")
                exit(0)
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
                    "INSERT":[],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Progress":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":[],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
                "Goals":{
                    "SELECT":["SELECT *", "SELECT BY ID"],
                    "INSERT":[],
                    "UPDATE":["UPDATE BY ID"],
                    "DELETE":["DELETE BY ID"]
                },
             }

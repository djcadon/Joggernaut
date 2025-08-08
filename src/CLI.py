from db_config import connect_db
#Standard library imports
import sys
from werkzeug.security import generate_password_hash, check_password_hash
#Global variables
selected_table = None
user_operation = None
#Dictionary to map table numbers to names
tables = {  
            1:"Users",
            2:"User_Metrics",
            3:"Friends",
            4:"Workouts",
            5:"Exercises",
            6:"Workout_Exercises",
            7:"Progress",
            8:"Goals"
         }
#Dictionary to map operations for each table
operations = {  
                "Users":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "User_Metrics":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID", "3:SELECT BY USERID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "Friends":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "Workouts":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID", "3:SELECT BY USERID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "Exercises":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID", "3:SELECT BY USERID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "Workout_Exercises":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "Progress":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID", "3:SELECT BY USERID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
                "Goals":{
                    "SELECT":["1:SELECT *", "2:SELECT BY ID", "3:SELECT BY USERID"],
                    "INSERT":["1:INSERT"],
                    "UPDATE":["1:UPDATE BY ID"],
                    "DELETE":["1:DELETE BY ID"]
                },
             }
#Dictionary to map tables to their respective names and schemas in the database 
db_tables = {
                "Users":{"users":["name", "password", "dob"]},
                "User_Metrics":{"user_metrics":["uid", "weight", "height"]},
                "Friends":{"friends":["fid", "uid"]},
                "Workouts":{"workouts":["uid", "name", "days_of_week"]},
                "Exercises":{"exercises":["uid", "name", "description"]},
                "Workout_Exercises":{"workout_exercises":["wid", "eid"]},
                "Progress":{"progress":["uid", "eid", "wid", "weight", "duration_mins"]},
                "Goals":{"goals":["uid", "goal_weight"]}
            }
#CASE HANDLING FUNCTIONS
#Function to handle user input for table selection
def handle_tables():
    print("Available Tables:\n")
    #Display available tables
    for key, value in enumerate(tables.items(), start=1):
        print(f"{key}. {value[1]}")
    print("\nEnter which table you want to interact with or 'exit' to quit:")
    #Loop to handle user input for table selection
    while True:
        global selected_table #Using global variable to store selected table
        user_input = input().strip().lower()
        match user_input:
            #Users table
            case "1":
                print("You selected Users table.")
                selected_table = 1
                return
            #User Metrics table
            case "2":
                print("You selected User Metrics table.")
                selected_table = 2
                return
            #Friends table
            case "3":
                print("You selected Friends table.")
                selected_table = 3
                return
            #Workouts table
            case "4":
                print("You selected Workouts table.")
                selected_table = 4
                return
            #Exercises table
            case "5":
                print("You selected Exercises table.")
                selected_table = 5
                return
            #Exercise_Workout table
            case "6":
                print("You selected Workout_Exercises table.")
                selected_table = 6
                return
            #Progress table
            case "7":
                print("You selected Progress table.")
                selected_table = 7
                return
            #Goals table
            case "8":
                print("You selected Goals table.")
                selected_table = 8
                return
            #Exit the CLI
            case 'exit':
                print("Exiting the CLI. Goodbye!")
                exit(0)
            #Invalid input
            case _:
                print("Invalid input. Please try again.")
#Function to handle user input for operation selection
def handle_operations(selected_table):
    global user_operation #Using global variable to store user operation
    table_name = tables[selected_table]
    print(f"Available operations for {table_name} table:")
    print("0. Main Menu")
    for key, value in enumerate(operations[table_name].keys(), start=1):
        print(f"{key}. {value}")
    print("\nEnter which operation you want to perform or 'exit' to quit:")
    #Loop to handle user input for operations
    while True:
        user_input = input().strip().lower()
        match user_input:
            #Main Menu option
            case "0":
                print("Returning to Main Menu.")
                user_operation = "0"
                return
            #SELECT operation
            case "1":
                print("Available SELECT options:")
                for option in operations[table_name]["SELECT"]:
                    print(f"{option}")
                user_operation = "1"
                return
            #INSERT operation
            case "2":
                print("Available INSERT options:")
                for option in operations[table_name]["INSERT"]:
                    print(f"{option}")
                user_operation = "2"
                return
            #UPDATE operation
            case "3":
                print("Available UPDATE options:")
                for option in operations[table_name]["UPDATE"]:
                    print(f"{option}")
                user_operation = "3"
                return
            #DELETE operation
            case "4":
                print("Available DELETE options:")
                for option in operations[table_name]["DELETE"]:
                    print(f"{option}")
                user_operation = "4"
                return
            #Exit the CLI
            case 'exit':
                print("Exiting the CLI. Goodbye!")
                exit(0)
            #Invalid input
            case _:
                print("Invalid input. Please try again.")
#Function to handle user input after operation
def handle_post_operation(selected_table, operation):
    #Get the table name from the selected table number
    table_name = tables[selected_table]
    table_name = db_tables[table_name].keys()
    table_name = list(table_name)[0]
    print("\nEnter which operation you want to perform or 'exit' to quit:")
    while True:
        user_input = input().strip().lower()
        final_operation = operation + user_input.strip().lower()
        match final_operation:
            #Return to Main Menu
            case _ if "0" in final_operation:
                print("Returning to Main Menu.")
            #SELECT * operation
            case "11":
                print(f"You selected SELECT * operation on {table_name} table.\n")
                select_all(table_name)
                break
            #SELECT BY ID operation
            case "12":
                print(f"You selected SELECT BY ID operation on {table_name} table.\n")
                record_id = input("Enter the ID of the record you want to select: ")
                select_by_id(table_name, record_id)
                break
            #SELECT BY USERID operation
            case "13":
                print(f"You selected SELECT BY USERID operation on {table_name} table.\n")
                user_id = input("Enter the UserID you want to select: ")
                select_by_userid(table_name, user_id)
                break
            #INSERT operation
            case "21":
                print(f"You selected INSERT operation on {table_name} table.\n")
                insert_record(selected_table)
                break
            #UPDATE operation 
            case "31":
                print(f"You selected UPDATE operation on {table_name} table.\n")
                record_id = input("Enter the ID of the record you want to update: ")
                update_record(selected_table, record_id)
                break
            #DELETE operation
            case "41":
                print(f"You selected DELETE operation on {table_name} table.\n")
                record_id = input("Enter the ID of the record you want to delete: ")
                delete_by_id(table_name, record_id)
                break
            #Exit the CLI
            case 'exit':
                print("Exiting the CLI. Goodbye!")
                exit(0)
            #Invalid input
            case _:
                print("Invalid input. Please try again.")
                final_operation = operation
                continue
#DATABASE OPERATIONS FUNCTIONS
#Function to select all records from a table
def select_all(table):
    cur, conn = connect_db()
    query = f"SELECT * FROM {table}"
    try:
        cur.execute(query)
        rows = cur.fetchall()
        print(f"Data from {table}:")
        for row in rows:
            for key, value in row.items():
                print(f"{key}: {value}")
            print()
    except Exception as e:
        print("Error selecting all records:", e)
    finally:
        cur.close()
        conn.close()
#Function to select a record by ID from a table
def select_by_id(table, record_id):
    """Select a row by ID."""
    cur, conn = connect_db()
    query = f"SELECT * FROM {table} WHERE id = %s"
    try:
        cur.execute(query, (record_id,))
        row = cur.fetchone()
        print(f"Record from {table} where id = {record_id}:")
        for key, value in row.items():
            print(f"{key}: {value}")
        print()
    except Exception as e:
        print("Error selecting record by ID:", e)
    finally:
        cur.close()
        conn.close()
#Function to select records by UserID from a table
def select_by_userid(table, user_id):
    cur, conn = connect_db()
    query = f"SELECT * FROM {table} WHERE uid = %s"
    try:
        cur.execute(query, (user_id,))
        rows = cur.fetchall()
        print(f"Records from {table} where uid = {user_id}:")
        for row in rows:
            for key, value in row.items():
                print(f"{key}: {value}")
            print()
    except Exception as e:
        print("Error selecting records by UserID:", e)
    finally:
        cur.close()
        conn.close()
#Function to insert a new record into a table dynamically
def insert_record(selected_table):
    cur, conn = connect_db()
    #Get friendly name and DB mapping
    friendly_name = tables[selected_table]
    db_table_name, columns = list(db_tables[friendly_name].items())[0]
    values = []
    for col in columns:
        value = input(f"Enter value for {col}: ")
        #Hash password before saving
        if col == "password":
            value = generate_password_hash(col)
        values.append(value)
    #Dynamically create placeholders
    placeholders = ", ".join(["%s"] * len(columns))
    col_names = ", ".join(columns)
    query = f"INSERT INTO {db_table_name} ({col_names}) VALUES ({placeholders})"
    try:
        cur.execute(query, values)
        conn.commit()
        print("Record inserted successfully.")
    except Exception as e:
        print("Insert failed:", e)
    finally:
        cur.close()
        conn.close()
#Function to update a record dynamically
def update_record(selected_table, record_id):
    cur, conn = connect_db()
    friendly_name = tables[selected_table]
    db_table_name, columns = list(db_tables[friendly_name].items())[0]
    print("Leave a field blank to skip updating it.")
    update_data = {}
    for col in columns:
        new_value = input(f"New value for {col} (blank to skip): ")
        if new_value != "":
            update_data[col] = new_value
    if not update_data:
        print("No fields to update.")
        return
    # Build SET clause dynamically
    set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
    values = list(update_data.values())
    values.append(record_id)  # For WHERE clause
    query = f"UPDATE {db_table_name} SET {set_clause} WHERE id = %s"
    try:
        cur.execute(query, values)
        conn.commit()
        print("Record updated successfully.")
    except Exception as e:
        print("Update failed:", e)
    finally:
        cur.close()
        conn.close()
#Function to delete a record by ID from a table
def delete_by_id(table, record_id):
    cur, conn = connect_db()
    query = f"DELETE FROM {table} WHERE id = %s"
    try:
        cur.execute(query, (record_id,))
        conn.commit()
        print(f"Record with id {record_id} deleted from {table}.")
    except Exception as e:
        print("Error deleting record by ID:", e)
    finally:
        cur.close()
        conn.close()
#Main function to start the CLI
def main():
    while True:
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
        handle_tables()
        handle_operations(selected_table)
        if user_operation == "0":
            continue
        handle_post_operation(selected_table, user_operation)
        if user_operation == "0":
            continue
        print("\nOperation completed. Would you like to do another\n")
        another = None
        while another != "y" and another != "n":
            another = input("Enter 'y' to continue or 'n' to exit: ").strip().lower()
            if another == 'n':
                print("Exiting the CLI. Goodbye!")
                exit(0)
            if another != "y" and another != "n":
                print("Invalid input. Please enter 'y' or 'n'.")
#Entry point for the script
if __name__ == "__main__":
    sys.exit(int(main() or 0))
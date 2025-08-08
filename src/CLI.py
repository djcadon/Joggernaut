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

tables = {
    1: "Users",
    2: "User Metrics",
    3: "Friends",
    4: "Workouts",
    5: "Exercises",
    6: "Exercise_Workout",
    7: "Progress",
    8: "Goals"
}

operations = {
    "Users": {
        "SELECT": ["SELECT *", "SELECT BY ID"],
        "INSERT": ["Name", "Password", "Date Of Birth"],
        "UPDATE": ["UPDATE BY ID"],
        "DELETE": ["DELETE BY ID"]
    },
    "User Metrics": {
        "SELECT": ["SELECT *", "SELECT BY ID"],
        "INSERT": ["Weight", "Height"],
        "UPDATE": ["UPDATE BY ID"],
        "DELETE": ["DELETE BY ID"]
    },
    # ... (rest same as before)
    "Goals": {
        "SELECT": ["SELECT *", "SELECT BY ID"],
        "INSERT": ["UserID", "GoalWeight"],
        "UPDATE": ["UPDATE BY ID"],
        "DELETE": ["DELETE BY ID"]
    }
}

def select_table():
    print("Available Tables:")
    for key, value in tables.items():
        print(f"{key}. {value}")
    print("\nEnter table number or 'exit':")

    while True:
        user_input = input("Table: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            exit()
        if user_input.isdigit() and int(user_input) in tables:
            return tables[int(user_input)]
        else:
            print("Invalid input. Try again.")

def handle_operations(table):
    print(f"Available operations for {table}:")
    for i, op in enumerate(operations[table], start=1):
        print(f"{i}. {op}")
    print("Enter operation number or 'exit':")

    while True:
        choice = input("Operation: ").strip().lower()
        if choice == "exit":
            print("Exiting CLI.")
            exit()
        if choice == "1":
            handle_select(table)
            break
        elif choice == "2":
            handle_insert(table)
            break
        elif choice == "3":
            handle_update(table)
            break
        elif choice == "4":
            handle_delete(table)
            break
        else:
            print("Invalid input. Try again.")

def handle_select(table):
    print("1. SELECT *")
    print("2. SELECT BY ID")
    choice = input("Choice: ").strip()
    if choice == "1":
        print(f"SELECT * FROM {table}")
        print("(Mocked) Data...")
    elif choice == "2":
        id = input("Enter ID: ")
        print(f"SELECT * FROM {table} WHERE id = {id}")
    else:
        print("Invalid choice.")

def handle_insert(table):
    fields = operations[table]["INSERT"]
    data = {}
    for field in fields:
        data[field] = input(f"Enter {field}: ")
    cols = ', '.join(data.keys())
    vals = ', '.join([f"'{v}'" for v in data.values()])
    print(f"INSERT INTO {table} ({cols}) VALUES ({vals})")

def handle_update(table):
    id = input("Enter ID to update: ")
    fields = operations[table]["INSERT"]
    updates = []
    for field in fields:
        new_val = input(f"New value for {field}: ")
        updates.append(f"{field} = '{new_val}'")
    set_clause = ', '.join(updates)
    print(f"UPDATE {table} SET {set_clause} WHERE id = {id}")

def handle_delete(table):
    id = input("Enter ID to delete: ")
    print(f"DELETE FROM {table} WHERE id = {id}")

# Run the program
selected_table = select_table()
handle_operations(selected_table)



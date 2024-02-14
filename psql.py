import sqlite3

def create_table():
    connection = sqlite3.connect("registration.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL)
                    ''')
    connection.commit()
    connection.close()

def register_user(name, age):
    connection = sqlite3.connect("registration.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    connection.commit()
    connection.close()

def list_users():
    connection = sqlite3.connect("registration.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    connection.close()

def update_user(user_id, new_name, new_age):
    connection = sqlite3.connect("registration.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE users SET name=?, age=? WHERE id=?', (new_name, new_age, user_id))
    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = sqlite3.connect("registration.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    connection.commit()
    connection.close()

create_table()

while True:
    print("\nChoose an operation:")
    print("1 - Register user")
    print("2 - List users")
    print("3 - Update user")
    print("4 - Delete user")
    print("0 - Exit")

    choice = input("Enter the number of the desired operation: ")

    if choice == "1":
        name = input("Enter the user's name: ")
        age = int(input("Enter the user's age: "))
        register_user(name, age)

    elif choice == "2":
        list_users()

    elif choice == "3":
        user_id = int(input("Enter the ID of the user you want to update: "))
        new_name = input("Enter the new name: ")
        new_age = int(input("Enter the new age: "))
        update_user(user_id, new_name, new_age)

    elif choice == "4":
        user_id = input("Enter the ID of the user you want to delete: ")
        delete_user(user_id)

    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

import sqlite3
import os

# Function to initialize the database
def init_database():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    # Create the tasks table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# Function to display the menu
def display_menu():
    print("\nCommand Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

# Function to view the To-Do List
def view_todo_list():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    if tasks:
        print("\nTo-Do List:")
        for task in tasks:
            status = "Done" if task[2] == 1 else "Pending"
            print(f"{task[0]}. {task[1]} - {status}")
    else:
        print("To-Do List is empty.")

# Function to add a task to the To-Do List
def add_task():
    task = input("Enter the task: ")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (task, status) VALUES (?, 0)", (task,))

    conn.commit()
    conn.close()

    print("Task added successfully.")

# Function to update the status of a task in the To-Do List
def update_task_status():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to update status: "))
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        if 1 <= task_number <= len(tasks):
            current_status = tasks[task_number - 1][2]
            new_status = 1 - current_status  # Toggle status (0 to 1, 1 to 0)
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, tasks[task_number - 1][0]))
            conn.commit()
            conn.close()
            print("Task status updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to delete a task from the To-Do List
def delete_task():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to delete: "))
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        if 1 <= task_number <= len(tasks):
            cursor.execute("DELETE FROM tasks WHERE id = ?", (tasks[task_number - 1][0],))
            conn.commit()
            conn.close()
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main function to run the To-Do List application
def main():
    init_database()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

import csv
import os

TODOS_FILE = "todos.csv"
todos = []


def add_one_task(title):
    """Add a new task to the in-memory task list."""
    todos.append(title)


def print_list():
    """Display all tasks with their numeric position."""
    if not todos:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for index, title in enumerate(todos, start=1):
        print(f"{index}. {title}")
    print()


def delete_task(number_to_delete):
    """Remove one task by its 1-based position in the list."""
    if number_to_delete < 1 or number_to_delete > len(todos):
        print("Invalid task number.")
        return False

    removed = todos.pop(number_to_delete - 1)
    print(f"Deleted: {removed}")
    return True


def save_todos():
    """Persist tasks into todos.csv."""
    with open(TODOS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title"])
        for title in todos:
            writer.writerow([title])


def load_todos():
    """Read tasks from todos.csv into memory."""
    todos.clear()
    if not os.path.exists(TODOS_FILE):
        return

    with open(TODOS_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        return

    # Skip header row if present
    start = 1 if rows[0] and rows[0][0].strip().lower() == "title" else 0
    for row in rows[start:]:
        if row and row[0].strip():
            todos.append(row[0].strip())


def show_menu():
    print("=== Task Manager ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    load_todos()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            add_one_task(title)
            save_todos()
            print(f"Added: {title}")

        elif choice == "2":
            print_list()

        elif choice == "3":
            print_list()
            if not todos:
                continue
            raw = input("Number to delete: ").strip()
            if not raw.isdigit():
                print("Please enter a valid number.")
                continue
            if delete_task(int(raw)):
                save_todos()

        elif choice == "4":
            save_todos()
            print("Saved. Goodbye!")
            break

        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

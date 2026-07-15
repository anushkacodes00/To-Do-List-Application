from datetime import datetime

from task_manager import add_task, complete_task, view_tasks


def show_header():
    """Display application header."""
    today = datetime.now()

    print("=" * 50)
    print("         SMART TO-DO LIST")
    print("=" * 50)
    print(f"Date : {today.strftime('%d %B %Y')}")
    print(f"Day  : {today.strftime('%A')}")
    print("=" * 50)


def show_menu():
    """Display main menu."""
    print("\n1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Exit")


def main():
    while True:
        show_header()
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("\nThank you for using Smart To-Do List.")
            print("Have a productive day!")
            break
        else:
            print("\nInvalid choice! Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
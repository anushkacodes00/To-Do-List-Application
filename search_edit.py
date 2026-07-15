from storage import load_tasks, save_tasks


def search_task():
    """
    Search tasks by task name.
    """

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo Tasks Available.")
        return

    keyword = input("\nEnter task name to search: ").lower()

    found = False

    print("\n========== SEARCH RESULT ==========")

    for task in tasks:

        if keyword in task["task"].lower():

            found = True

            print("-" * 50)
            print("ID       :", task["id"])
            print("Task     :", task["task"])
            print("Date     :", task["date"])
            print("Time     :", task["time"])
            print("Priority :", task["priority"])
            print("Status   :", task["status"])

    if not found:
        print("\nNo matching task found.")


def edit_task():
    """
    Edit task details.
    """

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo Tasks Available.")
        return

    print("\n========== TASK LIST ==========")

    for task in tasks:
        print(f"{task['id']}. {task['task']}")

    try:

        task_id = int(input("\nEnter Task ID to Edit: "))

        for task in tasks:

            if task["id"] == task_id:

                print("\nWhat do you want to edit?")

                print("1. Task Name")
                print("2. Date")
                print("3. Time")
                print("4. Priority")
                print("5. Cancel")

                choice = input("\nEnter choice: ")

                if choice == "1":
                    task["task"] = input("Enter New Task Name: ")

                elif choice == "2":
                    task["date"] = input("Enter New Date (YYYY-MM-DD): ")

                elif choice == "3":
                    task["time"] = input("Enter New Time (HH:MM): ")

                elif choice == "4":

                    print("\nPriority")
                    print("1. High")
                    print("2. Medium")
                    print("3. Low")

                    p = input("Choose Priority: ")

                    if p == "1":
                        task["priority"] = "High"

                    elif p == "2":
                        task["priority"] = "Medium"

                    else:
                        task["priority"] = "Low"

                elif choice == "5":
                    print("\nEdit Cancelled.")
                    return

                else:
                    print("\nInvalid Choice.")
                    return

                save_tasks(tasks)

                print("\nTask Updated Successfully!")
                return

        print("\nTask ID Not Found.")

    except ValueError:
        print("\nInvalid Input.")
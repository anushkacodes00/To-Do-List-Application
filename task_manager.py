from storage import load_tasks, save_tasks


def add_task():
    """Add a new task to the task list."""
    tasks = load_tasks()

    print("\n==== Add New Task ====")

    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("\nTask name cannot be empty.")
        return

    task_date = input("Enter task date (YYYY-MM-DD): ").strip() or "Not set"
    task_time = input("Enter task time (HH:MM): ").strip() or "Not set"
    priority = input("Enter task priority (Low/Medium/High): ").strip().capitalize() or "Medium"

    if len(tasks) == 0:
        task_id = 1
    else:
        task_id = tasks[-1]["id"] + 1

    task = {
        "id": task_id,
        "task": task_name,
        "date": task_date,
        "time": task_time,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(task)

    save_tasks(tasks)
    print("\nTask Added Successfully!")


def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo Tasks Available.")
        return

    print("\n================ ALL TASKS ================")
    print("{:<5} {:<25} {:<12} {:<8} {:<10} {:<12}".format(
        "ID", "Task", "Date", "Time", "Priority", "Status"
    ))
    print("-" * 80)

    for task in tasks:
        print("{:<5} {:<25} {:<12} {:<8} {:<10} {:<12}".format(
            task["id"],
            task["task"],
            task["date"],
            task["time"],
            task["priority"],
            task["status"]
        ))


def complete_task():
    """Mark a task as completed."""
    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo Tasks Available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter Task ID to Complete: "))
    except ValueError:
        print("\nInvalid Input.")
        return

    found = False

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Completed":
                print("\nTask is already completed.")
                return

            task["status"] = "Completed"
            found = True
            break

    if found:
        save_tasks(tasks)
        print("\nTask Completed Successfully!")
    else:
        print("\nTask ID not found.")

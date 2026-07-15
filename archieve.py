from storage import load_tasks


def view_archived_tasks():
    """
    Display all completed (archived) tasks.
    """

    tasks = load_tasks()

    archived_tasks = []

    for task in tasks:
        if task["status"] == "Completed":
            archived_tasks.append(task)

    if len(archived_tasks) == 0:
        print("\nNo Archived Tasks.")
        return

    print("\n========== ARCHIVED TASKS ==========")

    print("{:<5} {:<25} {:<12} {:<8} {:<10} {:<12}".format(
        "ID", "Task", "Date", "Time", "Priority", "Status"
    ))

    print("-" * 80)

    for task in archived_tasks:

        print("{:<5} {:<25} {:<12} {:<8} {:<10} {:<12}".format(
            task["id"],
            task["task"],
            task["date"],
            task["time"],
            task["priority"],
            task["status"]
        ))
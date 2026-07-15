from storage import load_tasks


def view_pending_tasks():
    """
    Display all pending tasks.
    """

    tasks = load_tasks()

    pending_tasks = []

    for task in tasks:
        if task["status"] == "Pending":
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("\nNo Pending Tasks.")
        return

    print("\n========== PENDING TASKS ==========")

    print("{:<5} {:<25} {:<12} {:<8} {:<10} {:<12}".format(
        "ID", "Task", "Date", "Time", "Priority", "Status"
    ))

    print("-" * 80)

    for task in pending_tasks:

        print("{:<5} {:<25} {:<12} {:<8} {:<10} {:<12}".format(
            task["id"],
            task["task"],
            task["date"],
            task["time"],
            task["priority"],
            task["status"]
        ))
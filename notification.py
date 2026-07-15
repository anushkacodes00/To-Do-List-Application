from datetime import datetime, timedelta
from time import sleep
from plyer import notification

from storage import load_tasks

# Keeps track of reminders already sent
sent_notifications = set()


def send_notification(title, message):
    """
    Display a desktop notification.
    """

    notification.notify(
        title=title,
        message=message,
        timeout=10
    )


def check_reminders():
    """
    Check all pending tasks and send a reminder
    15 minutes before the scheduled time.
    """

    tasks = load_tasks()

    current_time = datetime.now()

    for task in tasks:

        # Ignore completed tasks
        if task["status"] != "Pending":
            continue

        try:
            # Convert date and time into datetime object
            task_datetime = datetime.strptime(
                f"{task['date']} {task['time']}",
                "%Y-%m-%d %H:%M"
            )

            reminder_time = task_datetime - timedelta(minutes=15)

            # Unique key for each reminder
            notification_key = (
                task["id"],
                task_datetime.strftime("%Y-%m-%d %H:%M")
            )

            # Send notification only once
            if (
                reminder_time <= current_time < reminder_time + timedelta(seconds=30)
                and notification_key not in sent_notifications
            ):

                send_notification(
                    "⏰ Task Reminder",
                    f"{task['task']} starts in 15 minutes!"
                )

                sent_notifications.add(notification_key)

        except ValueError:
            print(f"Invalid date or time format for Task ID {task['id']}")


def start_notification_service():
    """
    Run the reminder service continuously.
    """

    while True:

        check_reminders()

        # Check every 30 seconds
        sleep(30)
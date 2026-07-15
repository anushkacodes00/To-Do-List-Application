import json
import os

# Path of the JSON file
FILE_NAME = "data/tasks.json"


def load_tasks():
    """
    Load tasks from the JSON file.
    Returns a list of tasks.
    """

    # If the file doesn't exist, create it
    if not os.path.exists(FILE_NAME):
        os.makedirs("data", exist_ok=True)

        with open(FILE_NAME, "w") as file:
            json.dump([], file, indent=4)

        return []

    # Read tasks from file
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        # If JSON is empty or corrupted
        return []


def save_tasks(tasks):
    """
    Save the task list to the JSON file.
    """

    os.makedirs("data", exist_ok=True)

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
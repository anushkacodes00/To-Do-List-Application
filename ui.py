import os

def clear_screen():
    """
    Clear the terminal screen.
    """

    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    """
    Display a formatted header.
    """

    print("=" * 50)
    print(title.center(50))
    print("=" * 50)

def print_success(message):
    """
    Display success message.
    """

    print(f"\n[SUCCESS] {message}")

def print_error(message):
    """
    Display error message.
    """

    print(f"\n[ERROR] {message}")

def print_info(message):
    """
    Display information message.
    """

    print(f"\n[INFO] {message}")

def pause():
    """
    Pause the program until user presses Enter.
    """

    input("\nPress Enter to continue...")
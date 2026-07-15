import calendar


def show_calendar():
    """
    Display a monthly calendar.
    """

    print("\n===== CALENDAR VIEW =====")

    try:
        year = int(input("Enter Year (YYYY): "))
        month = int(input("Enter Month (1-12): "))
        date = int(input("Enter Date (1-31): "))
        
        if month < 1 or month > 12:
            print("\nInvalid Month!")
            return

        print()
        print(calendar.month(year, month))

    except ValueError:
        print("\nPlease enter valid numbers.")
from datetime import datetime


def get_current_date():
    """
    Return today's date.
    """

    return datetime.now().strftime("%d %B %Y")


def get_current_day():
    """
    Return today's day.
    """

    return datetime.now().strftime("%A")


def validate_date(date):
    """
    Validate date format YYYY-MM-DD.
    """

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_time(time):
    """
    Validate time format HH:MM.
    """

    try:
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False
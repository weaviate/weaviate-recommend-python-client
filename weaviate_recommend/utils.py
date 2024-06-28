from datetime import datetime


def get_datetime() -> str:
    "Gets the current datetime in the format required by for Recommender"
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
    return formatted

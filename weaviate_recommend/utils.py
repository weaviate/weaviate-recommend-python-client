from datetime import datetime


def get_datetime() -> str:
    "Gets the current datetime in the format required by for Recommender"
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
    return formatted


def get_auth_header(api_key: str) -> dict:
    """
    Creates an authentication header with the given API key.
    """
    return {"Authorization": api_key, "Content-Type": "application/json"}

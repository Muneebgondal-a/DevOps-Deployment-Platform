import os
from datetime import datetime

HISTORY_FILE = "logs/history.txt"


def save_deployment():

    os.makedirs("logs", exist_ok=True)

    current_time = datetime.now()

    with open(HISTORY_FILE, "a") as file:

        file.write(
            f"Deployment completed at {current_time}\n"
        )


def get_history():

    if not os.path.exists(HISTORY_FILE):

        return []

    with open(HISTORY_FILE, "r") as file:

        return file.readlines()[::-1]
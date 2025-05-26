import json
import os

FILE_PATH = "chat_history.json"

# Ensure file exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        json.dump({}, f)


def load_history() -> dict:
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_history(history: dict):
    with open(FILE_PATH, "w") as f:
        json.dump(history, f, indent=4)


def get_user_history(user_id: str):
    history = load_history()
    return history.get(user_id, [])


def add_message(user_id: str, role: str, message: str):
    history = load_history()
    history.setdefault(user_id, []).append({"role": role, "message": message})
    save_history(history)
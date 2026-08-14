# memory.py

history = []


def add_message(role, content):

    history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_history():

    return history


def clear_history():

    global history

    history = []
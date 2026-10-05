sessions = [
    {"game": "Catan ", "player": "priya", "score": 6},
    {"game": "catan", "player": "priya", "score": 9},
    {"game": "CARCASSONNE", "player": "sam", "score": 11},
    {"game": "carcassonne", "player": "sam", "score": 4},
    {"game": "catan ", "player": "priya", "score": 3},
    {"game": "carcassonne", "player": "asha", "score": 1},
]

sorted(sessions, key=lambda session: session["game"])

sorted(sessions, key=lambda session: session["game"].strip().lower())

sorted(sessions, key=lambda session: (session["game"].strip().lower(), -session["score"]))


def sort_key(session):
    return (session["game"].strip().lower(), -session["score"])


sorted(sessions, key=sort_key)

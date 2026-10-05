sessions = [
    {"game": "Catan ", "player": "priya", "score": 6},
    {"game": "catan", "player": "priya", "score": 9},
    {"game": "CARCASSONNE", "player": "sam", "score": 11},
    {"game": "carcassonne", "player": "sam", "score": 4},
    {"game": "catan ", "player": "priya", "score": 3},
    {"game": "carcassonne", "player": "asha", "score": 1},
]

def sort_keys(session):
   return (session["game"].strip().lower(), -session["score"])

result = sorted(sessions, key=sort_keys)
print(result)







# result = sorted(sessions, key=lambda session: session["game"])

# result2 = sorted(sessions, key=lambda session: session["game"].strip().lower())

# result3 = sorted(sessions, key=lambda session: (session["game"].strip().lower(), -session["score"]))
# print(result3)

# def sort_key(session):
#     return (session["game"].strip().lower(), -session["score"])


# sorted(sessions, key=sort_key)

sessions = [
    {"game": "Catan ", "player": "priya", "score": 6},
    {"game": "catan", "player": "priya", "score": 9},
    {"game": "CARCASSONNE", "player": "sam", "score": 11},
    {"game": "carcassonne", "player": "sam", "score": 4},
    {"game": "catan ", "player": "priya", "score": 3},
    {"game": "carcassonne", "player": "asha", "score": 1},
]

scores_a = [s["score"] for s in sessions if s["game"].strip().lower() == "catan"]

scores_b = map(lambda s: s["score"],
               filter(lambda s: s["game"].strip().lower() == "catan", sessions))


# print(type(scores_a))
# print(type(scores_b))

# print(sum(scores_b))
# print(sum(scores_b))

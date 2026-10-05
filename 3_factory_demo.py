sessions = [
    {"game": "Catan ", "player": "priya", "score": 6},
    {"game": "catan", "player": "priya", "score": 9},
    {"game": "CARCASSONNE", "player": "sam", "score": 11},
    {"game": "carcassonne", "player": "sam", "score": 4},
    {"game": "catan ", "player": "priya", "score": 3},
    {"game": "carcassonne", "player": "asha", "score": 1},
]

def is_high_scorer(session, threshold):
    return session["score"] > threshold

high_scores_only = filter(lambda session: is_high_scorer(session, 10), sessions)

def make_classifier(threshold):
    def is_high_scorer(session) :
        return session["score"] > threshold
    return is_high_scorer

classify_5 = make_classifier(5)
classify_10 = make_classifier(10)

only_high_scores = list(filter(classify_10, sessions))

print(only_high_scores)
print(only_high_scores)
sessions = [
    {"game": "Catan ", "player": "priya", "score": 6},
    {"game": "catan", "player": "priya", "score": 9},
    {"game": "CARCASSONNE", "player": "sam", "score": 11},
    {"game": "carcassonne", "player": "sam", "score": 4},
    {"game": "catan ", "player": "priya", "score": 3},
    {"game": "carcassonne", "player": "asha", "score": 1},
]


def make_game_filter(game_name):
    normalised = game_name.strip().lower()
    def is_playing_game(session):
        return session["game"].strip().lower() == normalised
    return is_playing_game


is_catan = make_game_filter("catan")
is_carcassonne = make_game_filter("carcassonne")

print(filter(is_catan, sessions))

catan_sessions = list(filter(is_catan, sessions))
carcassonne_sessions = list(filter(is_carcassonne, sessions))

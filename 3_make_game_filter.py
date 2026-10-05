# 1. Write is_players_session(session, name), which returns True if the
#    session's player matches name.
# 2. Try filter(is_players_session, sessions). What goes wrong, and why?
# 3. Write make_player_filter(name), a factory that returns the original is_players_session function.
#    The returned function takes only a session, but remembers the name from the outer scope.
# 4. Create an instance of this function that returns all of the games Priya is playing with make_player_filter("priya") and store the result in a variable.
# 5. Pass is_priya to filter to get all of priya's sessions. Print the result.

def make_player_filter(name):
    def is_players_session(session):
        return session["player"] == name
    return is_players_session

is_priya = make_player_filter("priya")

priyas_sessions = list(filter(is_priya, sessions))

print(priyas_sessions)
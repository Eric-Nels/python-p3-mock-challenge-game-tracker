class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be non-empty string")
        
        if hasattr(self, "_title"):
            raise AttributeError("Title is immutable and cannot be changed after instantiation.")
        
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    def results(self):
        return self._results

    def players(self):
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        return sum(player_scores) / len(player_scores) if len(player_scores) > 0 else 0

class Player:
    def __init__(self, username):
        self._username = self._validate_username(username)
        self._result = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = self._validate_username(value)

    def _validate_username(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string.")
        return username

    def results(self):
        return self._result

    def games_played(self):
        return list(set(result.game for result in self._result))

    def played_game(self, game):
        return any(result.game == game for result in self._result)

    def num_times_played(self, game):
        return sum(1 for result in self._result if result.game == game)

class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000")
        
        if hasattr(self, "_score"):
            raise AttributeError("Score is immutable and cannot be changed after instantiation.")
        self.player = player
        self.game = game
        self._score = score

        Result.all.append(self)
        

        self.player._result.append(self)
        self.game._results.append(self)

    @property
    def score(self):
        return self._score
from brain_games.cli import welcome_user

MAX_ROUNDS = 3


def run_game(game):
    name = welcome_user()
    for _ in range(MAX_ROUNDS):
        game()
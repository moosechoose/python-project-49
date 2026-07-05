
from brain_games.cli import welcome_user

max_rounds = 3


def run_game(game):
    name = welcome_user()
    for _ in range(max_rounds):
        game()
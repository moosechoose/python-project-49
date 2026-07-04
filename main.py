import prompt
import importlib
from engine.core import run_game

def main():
    print("Hello from python-project-49!")
    match game:
        case "brain-even":
            game_module = importlib.import_module("scripts.brain_even")
        case "brain-calc":
            game_module = importlib.import_module("scripts.brain_calc")
    run_game(game_module.main)


if __name__ == "__main__":
    main()

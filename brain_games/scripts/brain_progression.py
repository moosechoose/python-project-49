from brain_games.engine import run_game
from brain_games.games.progression import brain_progression


def main():
    run_game({
        'rule': "What number is missing in the progression?",
        'make_round': brain_progression
    })


if __name__ == "__main__":
    main()
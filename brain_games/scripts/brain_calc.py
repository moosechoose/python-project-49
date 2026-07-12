from brain_games.engine import run_game
from brain_games.games.calc import brain_calc


def main():
    run_game({
        'rule': "What is the result of the expression?",
        'make_round': brain_calc
    })


if __name__ == "__main__":
    main()
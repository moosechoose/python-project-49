from brain_games.engine import run_game
from brain_games.games.gcd import brain_gcd


def main():
    run_game({
        'rule': "Find the greatest common divisor of given numbers.",
        'make_round': brain_gcd
    })


if __name__ == "__main__":
    main()
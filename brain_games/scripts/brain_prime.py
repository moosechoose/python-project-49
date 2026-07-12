from brain_games.engine import run_game
from brain_games.games.prime import brain_prime


def main():
    run_game({
        'rule': "/Answer \"yes\" if given number is prime. Otherwise answer \"no\"./",
        'make_round': brain_prime
    })


if __name__ == "__main__":
    main()

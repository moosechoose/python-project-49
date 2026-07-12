from brain_games.engine import run_game
from brain_games.games.even import brain_even


def main():
    run_game({
        'rule': "/Answer \"yes\" if the number is even, otherwise answer \"no\"./",
        'make_round': brain_even
    })


if __name__ == "__main__":
    main()
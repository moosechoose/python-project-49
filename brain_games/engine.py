import prompt

from brain_games.cli import welcome_user

MAX_ROUNDS = 3


def run_game(game):
    name = welcome_user()
    rule = game['rule']
    make_round = game['make_round']
    print(rule)
    correct_answers_in_row = 0
    for _ in range(MAX_ROUNDS):
        question, correct_answer = make_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")

        if answer == correct_answer:
            print("Correct!")
            correct_answers_in_row += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
        print(f"Congratulations, {name}!")

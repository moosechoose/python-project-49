import random

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    
    print("Answer 'yes' if number is even, otherwise answer 'no'")
    correct_answers_in_row = 0
    while correct_answers_in_row < 3:
        number = random.randint(1, 100)
        print(f"Question:{number}")
        answer = prompt.string("Your answer:")
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if answer == correct_answer:
            print("Correct!")
            correct_answers_in_row += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
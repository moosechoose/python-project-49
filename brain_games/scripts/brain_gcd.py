import random

import prompt

from brain_games.cli import welcome_user


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    name = welcome_user()
    
    print("Find the greatest common divisor of given numbers.")
    correct_answers_in_row = 0
    while correct_answers_in_row < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        print(f"Question: {number_1} {number_2}")
        answer = prompt.string("Your answer:")
        answer_int = int(answer.strip())
        correct_answer = gcd(number_1, number_2)
        if answer_int == correct_answer:
            print("Correct!")
            correct_answers_in_row += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    

if __name__ == "__main__":
    main()
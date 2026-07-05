import math
import random

import prompt

from brain_games.cli import welcome_user


def is_prime(number):
    if number < 2:
        return "no"
    if number == 2:
        return "yes"
    if number % 2 == 0:
        return "no"
    limit = math.isqrt(number)
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return "no"
    return "yes"


def main():
    name = welcome_user()
    
    print("/Answer \"yes\" if given number is prime. Otherwise answer \"no\"./")
    correct_answers_in_row = 0
    while correct_answers_in_row < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")   
        answer = prompt.string("Your answer:")
        correct_answer = is_prime(number)
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
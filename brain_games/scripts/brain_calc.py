import random

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    
    print("What is the result of the expression?")
    correct_answers_in_row = 0
    while correct_answers_in_row < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        symbol = random.choice(["+", "-", "*"])
        print(f"Question: {number_1} {symbol} {number_2}")
        answer = prompt.string("Your answer:")
        answer_int = int(answer.strip())
        if symbol == "+":
            correct_answer = number_1 + number_2
        elif symbol == "-":
            correct_answer = number_1 - number_2
        else: 
            correct_answer = number_1 * number_2
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
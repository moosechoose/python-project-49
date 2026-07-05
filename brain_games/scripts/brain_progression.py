import random

import prompt

from brain_games.cli import welcome_user


def progression():
    length = random.randint(5, 10) 
    start = random.randint(1, 50)
    step = random.randint(1, 10) * random.choice([-1, 1])
    progression = [start + i * step for i in range(length)]
    return progression


def missing_element(progression):
    missing_index = random.randint(0, len(progression) - 1)
    correct_value = progression[missing_index]
    changed_progression = progression.copy()
    changed_progression[missing_index] = ".."
    return changed_progression, correct_value


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    correct_answers_in_row = 0
    while correct_answers_in_row < 3:
        prog = progression()
        changed_prog, correct_answer = missing_element(prog)
        print(f"Question:{str(changed_prog)}")
        answer = prompt.string("Your answer:")
        answer_int = int(answer.strip())
        
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


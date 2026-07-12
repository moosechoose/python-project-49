import random


def brain_even():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer



import math
import random


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


def brain_prime():    
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = is_prime(number)
    return question, str(correct_answer)

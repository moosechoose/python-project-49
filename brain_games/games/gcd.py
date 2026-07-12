import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def brain_gcd():    
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = str(f"{number_1} {number_2}")
    correct_answer = gcd(number_1, number_2)
    return question, str(correct_answer)

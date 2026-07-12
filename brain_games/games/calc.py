import random


def brain_calc():    
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    symbol = random.choice(["+", "-", "*"])
    question = str(f"{number_1} {symbol} {number_2}")
    
    if symbol == "+":
        correct_answer = number_1 + number_2
    elif symbol == "-":
        correct_answer = number_1 - number_2
    else: 
        correct_answer = number_1 * number_2
    
    return question, str(correct_answer)

    


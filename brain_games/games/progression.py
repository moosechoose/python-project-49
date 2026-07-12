import random


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


def brain_progression():
    prog = progression()
    changed_prog, correct_answer = missing_element(prog)
    question = str(' '.join(map(str, changed_prog)))
    return question, str(correct_answer)
    
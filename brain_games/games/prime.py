import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def get_question_answer():

    question = random.randint(2, 70) # NOSONAR
    correct_answer = 'yes' if is_prime(question) else 'no'
    
    return question, str(correct_answer)


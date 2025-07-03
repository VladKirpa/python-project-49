from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no". '


def get_question_answer():
    question = randint(1, 20)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer

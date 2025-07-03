from random import choice, randint

RULES = 'What is the result of the expressions ?'


def get_question_answer():

    correct_answer = 0
    first_num = randint(0, 30)
    second_num = randint(0, 30)
    operator = choice(['*', '+', '-'])
    question = f'{first_num} {operator} {second_num}'

    match operator:
        case '+':
            correct_answer = first_num + second_num
        case '-':
            correct_answer = first_num - second_num
        case '*':
            correct_answer = first_num * second_num

    return question, str(correct_answer)


import random

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_answer():

    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    question = f'{first_num} {second_num}'
    correct_answer = 0

    if second_num == 0:
        correct_answer += first_num
    
    while second_num != 0:
        first_num, second_num = second_num, first_num % second_num
        if second_num == 0:
            correct_answer = first_num

    return question, str(correct_answer)


    

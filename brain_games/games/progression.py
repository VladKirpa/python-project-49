import random

RULES = 'What number is missing in the progression?'


def get_progression():
    
    first_num = random.randint(1, 40)  # NOSONAR
    second_num = random.randint(first_num + 20, first_num + 60)  # NOSONAR
    step = random.choice([2, 3, 4, 5])  # NOSONAR
    random_length = random.randint(5, 10)  # NOSONAR
    prepaired_list = []

    for i in range(first_num, second_num, step):
        if len(prepaired_list) != random_length:
            prepaired_list.append(str(i))
    
    return prepaired_list


def get_question_answer():
    correct_answer = ''
    question = get_progression()
    random_index = random.randint(1, len(question) - 1)  # NOSONAR

    correct_answer += str(question[random_index])
    question[random_index] = '..'
    question = ' '.join(question)

    return question, correct_answer


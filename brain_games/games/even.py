import prompt
import brain_games.cli as cli
from random import randint 
from brain_games.scripts.brain_engine import run_game


RULES = 'Answer "yes" if the number is even, otherwise answer "no". '


def get_question_answer():
    question = randint(1, 20)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer

def main():
    run_game()

if __name__ == '__main__':
    main()

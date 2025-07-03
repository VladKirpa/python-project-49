import prompt
import brain_games.cli as cli
from random import randint 

def main():
    cli.welcome_user()
    is_even_number()

def is_even_number():
    print(f'Answer "yes" if the number is even, otherwise answer "no". ')
    
    question_number = randint(1, 20)
    win_counter = 0

    while win_counter != 3:
    
        correct_answer = ''
        question_number = randint(1, 20)
        user_answer = prompt.string(f'Question: {question_number} \n Your answer : ')

        if question_number % 2 == 0:
            correct_answer += 'yes'
        elif question_number % 2 != 0:
            correct_answer += 'no'
        
        if user_answer == correct_answer:
                win_counter += 1
                print("Correct!")
        else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
                print(f"Let's try again {cli.name}")
                break
        
    if win_counter == 3:
         print(f'Congratulations, {cli.name}')
        
if __name__ == '__main__':
    main()

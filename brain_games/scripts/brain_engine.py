import prompt

import brain_games.cli as cli

ROUNDS = 3


def run_game(game):
    
    win_counter = 0
    cli.welcome_user()
    print(game.RULES)
    
    for _ in range(ROUNDS):
        question, correct_answer = game.get_question_answer()
        print(f'Question: {question}')
        
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}' \nLet's try again, {cli.name}!")
            break
        else: 
            win_counter += 1
            print('Correct!')
        
    if win_counter == 3:
        print(f'Congratulations, {cli.name}!')


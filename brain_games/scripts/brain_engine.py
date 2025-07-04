import prompt

import brain_games.cli as cli

ROUNDS = 3


def run_game(game):
    
    win_counter = 0
    cli.welcome_user()
    print(game.RULES)
    
    for _ in range(ROUNDS):
        question, corr = game.get_question_answer()
        print(f'Question: {question}')
        
        answer = prompt.string('Your answer: ')

        if answer != corr:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{corr}'")
            print(f"Let's try again, {cli.name}!")
            break
        else: 
            win_counter += 1
            print('Correct!')
        
    if win_counter == 3:
        print(f'Congratulations, {cli.name}!')


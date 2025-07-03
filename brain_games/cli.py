import prompt

name = None


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name ? ')
    print(f'Hello, {name}')




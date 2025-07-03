import prompt
from random import randint 
import brain_games.cli as cli
from brain_games.games import even
from brain_games.scripts.brain_engine import run_game

def main():
    run_game(even)

if __name__ == '__main__':
    main()


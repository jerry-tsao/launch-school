# Rock Paper Scissors Lizard Spock

# Note: The logical order of the choices is "rock, lizard, spock, scissors,
# paper". For the sake of familiarity, we will display the choices in the
# conventional order "rock, paper, scissors, lizard, spock".

import os
import random
from subprocess import call

VALID_CHOICES = ['rock', 'lizard', 'spock', 'scissors', 'paper']

SHORTENED_CHOICES = {
    'r': 'rock',
    'l': 'lizard',
    'sp': 'spock',
    'sc': 'scissors',
    'p': 'paper'
}

RULES = {
    ('scissors', 'paper'): 'Scissors cuts Paper',
    ('paper', 'rock'): 'Paper covers Rock',
    ('rock', 'lizard'): 'Rock crushes Lizard',
    ('lizard', 'spock'): 'Lizard poisons Spock',
    ('spock', 'scissors'): 'Spock smashes Scissors',
    ('scissors', 'lizard'): 'Scissors decapitates Lizard',
    ('lizard', 'paper'): 'Lizard eats Paper',
    ('paper', 'spock'): 'Paper disproves Spock',
    ('spock', 'rock'): 'Spock vaporizes Rock',
    ('rock', 'scissors'): 'Rock crushes Scissors'
}

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def display_welcome_banner():
    print()
    print('-----------------------------------')
    print()
    print('             WELCOME TO')
    print('         ROCK PAPER SCISSORS')
    print('            LIZARD SPOCK')
    print()
    print('-----------------------------------')
    print()
    print('   Rules:')
    print()

    for rule in RULES.values():
        print(f'   - {rule}')

    print()
    print('-----------------------------------')
    print()

def display_scores(scores):
    print('   Scores:')
    print()
    print(f'   Player: {scores['player']}')
    print(f'   Computer: {scores['computer']}')
    print()
    print(f'   Rounds played: {sum(scores.values())}')
    print()
    print('-----------------------------------')
    print()

def prompt(message):
    print(message)

def blank_line():
    print()

def display_mode_selector():
    prompt('Choose the mode: (1) Continuous play\n'
           '                 (2) Best of five')
    blank_line()

def choose_mode():
    while True:
        mode_input = input('Mode: ')
        mode_cleaned = mode_input.strip(' ()')
        blank_line()

        if mode_cleaned in ['1', '2']:
            break

        prompt(f'{mode_input} is an invalid choice.')

    return mode_cleaned

def get_player_choice():
    prompt('Choose one: (r)  Rock\n'
           '            (p)  Paper\n'
           '            (sc) Scissors\n'
           '            (l)  Lizard\n'
           '            (sp) Spock')
    blank_line()

    while True:
        player_input = input('Your choice: ')
        player_input_lower = player_input.lower().strip(' ()')
        blank_line()

        if (player_input_lower in SHORTENED_CHOICES or
            player_input_lower in VALID_CHOICES):
            break

        prompt(f'{player_input} is an invalid choice.')

    player_choice = (player_input_lower if player_input_lower in VALID_CHOICES
                     else SHORTENED_CHOICES[player_input_lower])

    return player_choice

def get_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)

    return computer_choice

def determine_winner(player, computer):
    player_choice_index = VALID_CHOICES.index(player)
    player_choice_wins = [(VALID_CHOICES.index(player) + 1) %
                          len(VALID_CHOICES),
                          (VALID_CHOICES.index(player) + 3) %
                          len(VALID_CHOICES)]
    computer_choice_index = VALID_CHOICES.index(computer)

    if player_choice_index == computer_choice_index:
        winner = 'tie'
    elif computer_choice_index in player_choice_wins:
        winner = 'player'
    else:
        winner = 'computer'

    return winner

def display_winner(player_choice, computer_choice, winner):
    prompt(f'You chose {player_choice.title()}, '
           f'computer chose {computer_choice.title()}.')
    blank_line()

    if winner == 'player':
        rule = RULES[player_choice, computer_choice]
        prompt(f'{rule}!')
        blank_line()
        prompt('You win!')
    elif winner == 'computer':
        rule = RULES[computer_choice, player_choice]
        prompt(f'{rule}!')
        blank_line()
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

    blank_line()

def display_grand_winner(scores):
    if scores['player'] > scores['computer']:
        print('You are the grand winner!')
    elif scores['player'] < scores['computer']:
        print('The computer is the grand winner!')
    else:
        print('It\'s a draw!')

    blank_line()

def reset_scores():
    scores = {'player': 0, 'computer': 0, 'tie': 0}

    return scores

def update_scores(scores, winner):
    scores[winner] += 1

    return scores

def play_rpsls(scores):
    clear()
    display_welcome_banner()
    display_scores(scores)

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(player_choice, computer_choice)
    scores = update_scores(scores, winner)

    clear()
    display_welcome_banner()
    display_scores(scores)
    display_winner(player_choice, computer_choice, winner)

def check_y_n():
    while True:
        answer = input('(y/n): ')
        answer_lower = answer.lower().strip(' ()')
        blank_line()

        if answer_lower in ('y', 'yes', 'n', 'no'):
            break

        prompt(f'{answer} is an invalid response.')
        prompt('Please enter "y" or "n".')

    return answer_lower[0]

def play_again(scores, mode):
    while True:
        prompt('Do you want to play again? (y/n)')

        answer = check_y_n()

        if answer == 'n':
            clear()
            break

        if mode == '1':
            play_rpsls(scores)
        else:
            main()
            break

def next_round():
    input('Press enter to play the next round...')

def continuous_play(scores):
    play_rpsls(scores)
    play_again(scores, '1')

def best_of_five(scores):
    rounds = 0

    while rounds < 5:
        play_rpsls(scores)
        rounds = sum(scores.values())

        if rounds < 5:
            next_round()

    display_grand_winner(scores)
    play_again(scores, '2')

def main():
    scores = reset_scores()

    clear()
    display_welcome_banner()
    display_mode_selector()

    mode = choose_mode()

    if mode == '1':
        continuous_play(scores)
    else:
        best_of_five(scores)

if __name__ == '__main__':
    main()

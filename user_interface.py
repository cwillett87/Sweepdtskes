import os


def validate_main_menu(user_input):
    switcher = {
        1: (True, 1),
        2: (True, 2)
    }
    return switcher.get(user_input, (False, None))


def name_firm():
    print("Let's create a marketing firm!  In order to get started, please enter a name for the firm: ")


#prompt which manager would you like to use?
def marketing_firm_menu():
# 1 for stack or 2 for queue
    user_selection = (False, None)
    while user_selection[0] is False:
        print('What type of manager would you like to use?')
        print('Press 1 for Stack')  # input 1 = create stack manager
        print('Press 2 for Queue')  # input 2 = create queue manager
        user_input = try_parse_int(input())
        user_selection = validate_main_menu(user_input)
    return user_selection[1]


#prompt would you like to create a sweepstakes?
def sweepstakes_menu():
    print("Now let's create a sweepstake! What would you like the name to be? ")


#what would you like to name the sweepstakes?
def name_sweepstakes():
    print('Please enter a name for the sweepstake!')


#lets register some contestants
def registration():
    print('Please register a contestant! ')


#input first name, last name , email and assign a registration number
def contestant_registration_number():
    print('Please assign this contestant a unique registration number: ')


def contestant_first_name():
    print('What is the contestants first name? ')


def contestant_last_name():
    print('What is the contestants last name? ')


def contestant_email():
    print('What is the contestants email address? ')


#would you like to register another contestant?
def register_another_contestant():
    user_selection = (False, None)
    while user_selection[0] is False:
        print('Would you like to register another contestant?')
        print('Press 1 for yes')  #if yes continue to register
        print('Press 2 for no')  # no = terminate
        user_input = try_parse_int(input())
        user_selection = validate_main_menu(user_input)
    return user_selection[1]


#print all contestants
def show_contestants(contestants):# dependency injection works no matter which contestants are used
    print('Here all the registered contests in: ')
    print(' ')
    for key in contestants.items():
        li = list(key)
        print(f'Contestant registration number: {li[0]}, '
              f'First name: {li[1].first_name}, '
              f'Last name: {li[1].last_name}, '
              f'Email: {li[1].email}')
    print(' ')


def last_registration_number_used(contestants): # dependency injection works no matter which contestant is used
    print('Registration numbers used: ')
    for key in contestants.items():
        li = list(key)
        print(f'{li[0]}')


#if no move on to pick a winner
def prompt_pick_winner():
    print('Now that your done registering contestants, lets find out who wins!')
    print(' ')


def show_winner_info(contestant): # dependency injection works no matter which contestant is used
    print("AND...")
    print('The winning registration number is:  ', contestant[0])
    print(contestant[1].first_name + ' ' + contestant[1].last_name)
    print(f'Email: {contestant[1].email}')


def try_parse_int(value):
    try:
        return int(value)
    except:
        return 0


def clear_console():
    os.system('cls' if os.name == 'nt' else "clear")

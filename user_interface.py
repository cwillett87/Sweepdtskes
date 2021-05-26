import os

#would you like to create a marketing firm? yes or no
def simulation_main_menu():
    user_selection = (False, None)
    while user_selection[0] is False:
        print('Would you like to create a marketing firm?')
        print('Press 1 for yes') #yes = create marketing firm
        print('Press 2 for no') #no = terminate
        user_input = try_parse_int(input())
        user_selection = validate_main_menu(user_input)
    return user_selection[1]


def validate_main_menu(user_input):
    switcher = {
        1: (True, 1),
        2: (True, 2)
    }
    return switcher.get(user_input, (False, None))


def name_firm():
    print('Please name the marketing firm:')


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
#yes = create sweepstakes
#no = terminate

#if yes what would you like to name the sweepstakes?
#create sweepstakes with input name

#lets register some contestants
#input first name, last name , email and assign a registration number
#would you like to register another contestant?
#if yes continue to register
#if no move on to pisk a winner

#no = time to pick a winner
#press 1 to randomly pick a winner and notify the contestant
#press 2 to register more contestants

#prompt what would you like to do now?
#press 1 to create another marketing firm
#press 2 to choose another manager
#press 3 to create another sweepstakes
#press 4 to finish (print goodbye message)


def try_parse_int(value):
    try:
        return int(value)
    except:
        return 0


def clear_console():
    os.system('cls' if os.name == 'nt' else "clear")

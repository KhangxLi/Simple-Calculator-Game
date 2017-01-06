import sys
running = True
choosing = True

def main_menu():
    '''Main menu options.'''
    while running:
        print("\nChoose your desired operation:")
        print("\nEnter '1' = Addition")
        print("Enter '2' = Substraction")
        print("Enter '3' = Multiplication")
        print("Enter '4' = Division")
        print("Enter 'quit' = quit\n")
        cmd = str(input("Enter command : "))
        if cmd == '1':
            operation('Addition', '+')
        elif cmd == '2':
            operation('Substraction', '-')
        elif cmd == '3':
            operation('Multiplication', '*')
        elif cmd == '4':
            operation('Division', '/')
        elif cmd == 'quit':
            mainmenu_quit()
        elif cmd == 'hack':
            steinsgate()
        else:
            print('\n', "'", cmd, "'", "is not an option. But that's cool, you're thinking outside of the box\n")

def mainmenu_quit():
    '''When quitting at the main menu.'''
    print("Are you sure? 'yes' or 'no'")
    cmd = str(input("\nEnter command : "))
    if cmd == 'yes':
        print('Quit!' * 500000)
        sys.exit(0)
    elif cmd == 'no':
        print('\n What would you like to do?')
        main_menu()
    elif cmd == 'hack':
        steinsgate()
    else:
        print('\n', "'", cmd, "'", 'is not an option. Here are your choices:', '\n')
        main_menu()

def operation(woperator, soperator):
    '''Lets the user do an operation that will result in 69. Humour > 9000.'''
    print("\n", woperator)
    try:
        first = float(input("Enter first number :"))
        second = float(input("Enter second number :"))
        result = 69.0
        print('\n', first, soperator, second, '=', result, '\n')
        after_operation(woperator, soperator)
    except ValueError:
        print("Is that a number? Suit yourself...\n")
        first = str(input("Enter first number :"))
        second = str(input("Enter second number :"))
        result = 69.0
        print('\n', first, soperator, second, '=', result, '\n')
        after_operation(woperator, soperator)

def after_operation(woperator, soperator):
    '''Options after the operation.'''
    while choosing:
        print("Enter 'again' = Another", woperator)
        print("Enter 'back' for Menu")
        print("Enter 'quit' to quit\n")
        cmd = str(input("Enter command : "))
        if cmd == 'back':
            break
        elif cmd == 'quit':
            quitting(woperator, soperator)
            break
        elif cmd == 'again':
            operation(woperator, soperator)
            break
        elif cmd == 'hack':
            steinsgate()
        else:
            print("\n", "'", cmd, "'", "is not an option. Are you iliterate? Here's the menu.  \n")
            break
        #I do know how to write illiterate.

def quitting(woperator, soperator):
    '''Quitting when not at main menu.'''
    print("Are you sure? 'yes' or 'no'")
    cmd = str(input("\nEnter command : "))
    if cmd == 'yes':
        print('Quit!' * 500000)
        sys.exit(0)
    elif cmd == 'no':
        after_operation(woperator, soperator)
    elif cmd == 'hack':
        steinsgate()
    else:
        print('\n', "'", cmd, "'", 'is not an option. Why are you like this?', '\n')

def steinsgate():
    '''Fun reference to Steins;Gate.'''
    print(' El Psy Congroo' * 100000)

def welcome():
    '''Welcome message.'''
    print('WELCOME TO SIMPLE CALCULATOR \nPlease have fun with this SIMPLE CALCULATOR.')

welcome()
main_menu()

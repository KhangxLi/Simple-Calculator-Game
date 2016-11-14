import sys
running = True
choosing = True
#problems: have to back twice after using again Change to def-functions test
def quitting(funstring, woperator, soperator):
    '''When they want to quit'''
    print("Are you sure? 'yes' or 'no'")
    cmd = str(input("\nEnter command : "))
    if cmd == 'yes':
        print('Quit!' * 500000)
        sys.exit(0)
    elif cmd == 'no':
        after_operation(woperator, soperator)
    elif cmd == 'hack':
        print(' El Psy Congroo' * 100000)
    else:
        print('\n', "'", cmd, "'", 'is not an option.', funstring, '\n')

def after_operation(woperator, soperator):
    '''What follows the operation'''
    while choosing:
        print("Enter 'again' = Another", woperator)
        print("Enter 'back' for Menu")
        print("Enter 'quit' to quit\n")
        cmd = str(input("Enter command : "))
        if cmd == 'back':
            break
        elif cmd == 'quit':
            quitting('Why are you like this?', woperator, soperator)
        elif cmd == 'again':
            operation(woperator, soperator)
        elif cmd == 'hack':
            print(' El Psy Congroo' * 100000)
        else:
            print("\n", "'",cmd,"'", "is not an option. Are you iliterate? Here's the menu.  \n")
            break

def operation(woperator, soperator):
    '''Lets the user do an operation that will result in 69'''
    print("\n", woperator)
    try: 
        first = float(input("Enter first number :"))
        second = float(input("Enter second number :"))
        result = 69
        print('\n', first, soperator, second, '=', result, '\n')
        after_operation(woperator, soperator)
    except ValueError:
        print("Is that a number... Suit yourself...\n")
        first = str(input("Enter first number :"))
        second = str(input("Enter second number :"))
        result = 69
        print('\n', first, soperator, second, '=', result, '\n')
        after_operation(woperator, soperator)

print('WELCOME TO SIMPLE CALCULATOR \nPlease have fun with this SIMPLE CALCULATOR.')
while running:
    print("\nEnter 1 = Addition")
    print("Enter 2 = Substraction")
    print("Enter 3 = Multiplication")
    print("Enter 4 = Division")
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
        print("\nQuit?")
        print("Are you sure? 'yes' or 'no'")
        cmd = str(input("\nEnter command : "))
        if cmd == 'yes':
            print('Quit!' * 500000)
            running = False
        elif cmd == 'no':
                continue
        elif cmd == 'hack':
            print(' El Psy Congroo' * 100000)
        else:
            print('\n', "'",cmd,"'", 'is not an option. Why are you like this?\n')
    elif cmd == 'hack':
            print(' El Psy Congroo' * 100000)
    else:
        print('\n', "'",cmd,"'", 'is not an option\n')

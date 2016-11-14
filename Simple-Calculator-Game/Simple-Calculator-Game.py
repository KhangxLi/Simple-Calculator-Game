running = True
choosing = True
def operation(woperator, soperator):
    '''Lets the user do an operation that will result in 69'''
    print("\n", woperator)
    try: 
        first = float(input("Enter first number :"))
        second = float(input("Enter second number :"))
        result = 69
        print('\n', first, soperator, second, '=', result, '\n')
        print("Enter 'again' = Another", woperator)
        print("Enter 'back' for Menu")
        print("Enter 'quit' to quit\n")
    except ValueError:
        print("Is that a number... Doesn't matter, it should still work:\n")
        first = str(input("Enter first number :"))
        second = str(input("Enter second number :"))
        result = 69
        print('\n', first, soperator, second, '=', result, '\n')
        print("Enter 'again' = Another", woperator)
        print("Enter 'back' for Menu")
        print("Enter 'quit' to quit\n")

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
        cmd = str(input("Enter command : "))
        if cmd == 'back':
            continue
        elif cmd == 'again':
            operation('Addition', '+')
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
            print("\n", "'",cmd,"'", "is not an option. Are you iliterate? Here's the menu.  \n")

    elif (cmd == '2') or (cmd == '3') or (cmd == '4'):
        print('This module is not ready yet. Please choose another option.')

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
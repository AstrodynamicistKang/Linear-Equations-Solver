# This is just a test of Python programming skill. :)
# Created using Python 3.6.5
# Kindly report bugs should you come across any of them. Thanks!

# This Python program is a simulateneous linear equation solver.  

while True:
    print('Welcome to the linear equation solver. The linear equations defined are in the slope-intercept forms y = ax + b and y = cx + d respectively.')
    print()

    while True:
        print('Please enter the relevant constant values when prompted.')
        print()

        a = ''
        while a == '': 
            print('a = ', end = '')
            try:
                a = eval(input())
            except (NameError, SyntaxError):
                print('Please enter numerical values only.')
                a = ''

        b = ''
        while b == '':
            print('b = ', end = '')
            try:
                b = eval(input())
            except (NameError, SyntaxError):
                print('Please enter numerical values only.')
                b = ''

        c = ''
        while c == '':
            print('c = ', end = '')
            try:
                c = eval(input())
                if a == 0 and c == 0:
                    print()
                    print('Since a = 0, c MUST NOT equal to 0 or there will be no 2 simultaneous linear equations to be solved.')
                    print()
                    print('Please try again.')
                    c = ''
            except (NameError, SyntaxError):
                print('Please enter numerical values only.')
                c = ''

        d = ''
        while d == '':
            print('d = ', end = '')
            try:
                d = eval(input())
            except (NameError, SyntaxError):
                print('Please enter numerical values only.')
                d = ''
                
        while True:
            print()
            print('The equations are y = ' + str(a) + 'x+' + str(b) + ' and y = ' + str(c) + 'x+' + str(d) + '.')
            print()
            print('Confirm inputs? Y/N')

            confirm_input = str(input()).lower()
            
            if confirm_input == ('n' or 'no'):
                break
            elif confirm_input == ('y' or 'yes'):
                break
            else :
                print()
                print('Invalid input. Please enter yes/no.')
                continue
            
        if confirm_input == ('n' or 'no'):
            print()
            continue
        elif confirm_input == ('y' or 'yes'):
            break
            
    print()
    
    if a == c:
        if b == d:
            print('The 2 linear equations are exactly the same. There are infinitely many solutions.')
        if b != d:
            print('The 2 lines are parallel and they will never intersect in Euclidean space. There is no solution.')
    else :
        x = (d - b)/(a - c)
        print("The solution is x = " + str(x)+ ".")

    while True:
        print()
        print('Thanks for trying out the program. Would you like to try the program again with other linear equation(s).? Y/N')

        confirm_input = str(input()).lower()

        if confirm_input == ('n' or 'no'):
            print('Have a nice day then!')
            break
        elif confirm_input == ('y' or 'yes'):
            break
        else :
            print()
            print("Invalid input. Please enter 'Yes' or No'.")
            continue

    if confirm_input == ('n' or 'no'):
        break
    elif confirm_input == ('y' or 'yes'):
        print()
        continue

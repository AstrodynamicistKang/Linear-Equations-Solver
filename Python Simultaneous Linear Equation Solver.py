# This is just a test of Python programming skill. :)
# Created using Python 3.6.5
# Kindly report bugs should you come across any of them. Thanks!

# This Python program is a simulateneous linear equation solver.  

confirm_input = ''

while confirm_input == '':
    print('Welcome to the linear equation solver. The linear equations defined are in the slope-intercept forms y = ax + b and y = cx + d respectively.')
    print()

    confirm_input = ''

    while confirm_input == '' :
        print('Please enter the relevant constant values when prompted.')
        print()

##  The following codes determine if a user's input is a string. But it does not allow fraction inputs like 2/3 or
##  arithmetic experssions while doing assignments at the same time, such as x = 2+3
##      a = ''
##      while a == '':
##          print('a = ', end = '')
##          a = input()
##          if type(a) == str :
##              print('Please input a numerical value only.')

        
        print('a = ', end = '')
        a = eval(input())
                
        print('b = ', end = '')
        b = eval(input())
                
        c = ''
        while c == '':
            print('c = ', end = '')
            c = eval(input())
            if a == 0 and c == 0:
                print()
                print('Since a = 0, c MUST NOT equal to 0 or there will be no 2 simultaneous linear equations to be solved.')
                print()
                print('Please try again.')
                c = ''
        
        print('d = ', end = '')
        d = eval(input())

        confirm_input = 'Try Again'
        while confirm_input == 'Try Again' :
            print()
            print('The equations are y = ' + str(a) + 'x+' + str(b) + ' and y = ' + str(c) + 'x+' + str(d) + '.')
            print()
            print('Confirm inputs? Y/N')

            confirm_input = str(input())
            
            if confirm_input == 'n' :
                confirm_input = ''
                break
            elif confirm_input == 'no' :
                confirm_input = ''
                break
            elif confirm_input == 'No' :
                confirm_input = ''
                break
            elif confirm_input == 'nO' :
                confirm_input = ''
                break
            elif confirm_input == 'NO' :
                confirm_input = ''
                break
            elif confirm_input == 'N' :
                confirm_input = ''
                break
            elif confirm_input == 'y' :
                break
            elif confirm_input == 'yes' :
                break
            elif confirm_input == 'Yes' :
                break
            elif confirm_input == 'YEs' :
                break
            elif confirm_input == 'YeS' :
                break
            elif confirm_input =='YES' :
                break
            elif confirm_input =='Y' :
                break
            else :
                print()
                print('Invalid input. Please enter yes/no.')
                confirm_input = 'Try Again'
                continue
            
        if confirm_input == '' :
            print()
            continue


    # 'y' or 'yes' or 'Yes' or 'YEs' or 'YeS' or 'YeS' or 'YES' or 'Y' or 'n' or 'no' or 'No' or 'nO' or 'NO' or 'N' (Too lazy to copy so many words. So keep them here in case I need them.)

    print()
    
    if a == c:
        if b == d:
            print('The 2 linear equations are exactly the same. There are infinitely many solutions.')
        if b != d:
            print('The 2 lines are parallel and they will never intersect in Euclidean space. There is no solution.')
    else :
        x = (d - b)/(a - c)
        print("The solution is x = " + str(x)+ ".")

    confirm_input = 'Try Again'
    while confirm_input == 'Try Again':
        print()
        print('Thanks for trying out the program. Would you like to try the program again with other linear equation(s).? Y/N')

        confirm_input = str(input())

        if confirm_input == 'n' :
            print('Have a nice day then!')
            break
        elif confirm_input == 'no' :
            print('Have a nice day then!')
            break
        elif confirm_input == 'No' :
            print('Have a nice day then!')
            break
        elif confirm_input == 'nO' :
            print('Have a nice day then!')
            break
        elif confirm_input == 'NO' :
            print('Have a nice day then!')
            break
        elif confirm_input == 'N' :
            print('Have a nice day then!')
            break
        elif confirm_input == 'y' :
            confirm_input = ''
            break
        elif confirm_input == 'yes' :
            confirm_input = ''
            break
        elif confirm_input == 'Yes' :
            confirm_input = ''
            break
        elif confirm_input == 'YEs' :
            confirm_input = ''
            break
        elif confirm_input == 'YeS' :
            confirm_input = ''
            break
        elif confirm_input =='YES' :
            confirm_input = ''
            break
        elif confirm_input =='Y' :
            confirm_input = ''
            break
        else :
            print()
            print("Invalid input. Please enter 'Yes' or No'.")
            confirm_input = 'Try Again'
            continue
        
    if confirm_input == '':
        print()
        continue

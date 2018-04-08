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

        a = ''
        while a == '':
            print('a = ', end = '')
            a = eval(input())
            if a == '':
                print('Please enter a value for a.')

        a = float(a)

        b = ''
        while b == '':
            print('b = ', end = '')
            b = eval(input())
            if b == '':
                print('Please enter a value for b.')
                
        b = float(b)
                
        c = ''
        
        while c == '':
            print('c = ', end = '')
            c = eval(input())
            if (str(c) != ''):
                if (float(a) == (float(0)) and (float(c) == float(0))):
                    print()
                    print('Since a = 0, c MUST NOT equal to 0 or there will be no 2 simultaneous linear equations to be solved. An infinite loop will result.')
                    print()
                    print('Please try again.')
                    c = ''
            if c == '':
                    print('Please enter a value for c.')

        a = float(a)
        c = float(c)
        
        d = ''
        while d == '':
            print('d = ', end = '')
            d = eval(input())
            if d == '':
                print('Please enter a value for b.')
                
        d = float(d)

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

    print("""This solver works by inspecting convergence and divergence of y-values (delta y) for a given delta x. Convergence leads to a solution \
and divergence indicates no solution is present. Solution is the x-value obtained when the corresponding delta y is zero.""")

    print()

    confirm_input = ''

    while confirm_input == '' :
        print('Please enter an x0-value (initial x-value), configure the the step size (dx) and span (sp).')
        print()

        x0 = ''
        while x0 == '':
            print('x0 = ', end = '')
            x0 = eval(input())
            if x0 == '':
                print('Please enter a value for x0.')
                
        x0 = float(x0)

        dx = ''
        while dx == '' or float(0):
            print('dx = ', end = '')
            dx = eval(input())
            if dx == '' :
                print('Please enter a value for dx.')
            elif (float(dx) == float(0)):
                print('dx MUST never be zero or the solver cannot proceed. An infinite loop will result!')
                dx = ''

        dx = abs(float(dx))

        sp = ''
        while sp == '' or ((float(sp)) < (float(dx))):
            print('sp = ', end = '')
            sp = eval(input())      
            if sp == ('') :
                print('Please enter a value for sp.')
            elif ((float(sp)) < ((float(dx)))):
                print('sp MUST never be less than dx or the solver cannot proceed.')
                sp = ''
                
        sp = float(sp)

        confirm_input = 'Try Again'
        while confirm_input == 'Try Again' :
            print()
            print('You initiated x0 = ' + str(x0) + ', step size dx = ' + str(dx) + ' and span, sp = ' + str(sp) + '.')
            print('It is strongly advisable to begin with a large sp for extreme constant values of a, b, c and d, or the solution may not converge.')  
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

    print()

    y01 = (a)*(x0) + b
    y02 = (c)*(x0) + d
    x = x0

    PI = PE = PL = PD = PIS = PDS = ''
    

    while (x <= (x0 + sp)):
        y1 = (a)*(x) + b
        y2 = (c)*(x) + d 
        x = x + dx

        if (y1 > y2) or (y1 < y2) :
            continue

        elif (y2 - y1) == (y02 - y01) :
            if a == c :
                print(str(a) + ' = ' + str(c))
                print('Iterations with initiated x-value = ' + str(x0) + ' step size dx = ' + str(dx) + ' , and span, sp = ' + str(sp) + \
                      ' yields no solution for increasing x-values and the delta-y value is a constant for (x0 - sp) < x <= (x0 + sp).')
                print('The 2 lines are therefore parallel and they never intersect each other in Euclidean space.')
                PL = True
        
            else :
                print(str(a) + ' != ' + str(c))
                print('But the delta-y value is a constant for x <= (x0 + sp).')
                print('That means the x-value which you have initiated earlier is the x-value of the point of intersection itself!')
                print('The solution is x = ' + str(x0) + '.')
                PE = True
            break
                
        elif (y1 == y2) :
            x = x - dx
            print('Delta y converges for increasing x-values.\nThe solution is x = ' + str(x) + '.')
            PIS = True
            xPIS = str(x)
            break

    if (y1 != y2) and ((y2 - y1) != (y02 - y01)):
            
        if abs(y2 - y1) > abs(y02 - y01):
            print('Iterations with initiated x-value = ' + str(x0) + ' step size dx = ' + str(dx) + ' , and span, sp = ' + str(sp) + \
                  ' yields no solution and delta y diverges with increasing values of x.')
            PI = False
            print('Now trying by reducing x-values.')
            
        elif abs(y2 - y1) < abs(y02 - y01):
            print('Iterations with initiated x-value = '+ str(x0) + ' step size dx = ' + str(dx) + ' , and span, sp = ' + str(sp) + \
                  ' yields no solution and delta y converges with increasing values of x.')
            PI = True
            print('Now trying by reducing x-values.')
        else:
            print('Program error. Please kindly report the bug to the author. Thanks!')

    x = x0

##    while x >= (x0 - sp):
##        y1 = a*x + b
##        y2 = c*x + d 
##        x = x - dx

    while (x >= (x0 - sp)):
        y1 = (a)*(x) + b
        y2 = (c)*(x) + d 
        x = x - dx
        
        if (y1 > y2) or (y1 < y2) :
            continue

        elif (y2 - y1) == (y02 - y01) :
            if a == c :
                print(str(a) + ' = ' + str(c))
                print('Iterations with initiated x-value = ' + str(x0) + ' step size dx = ' + str(dx) + ' , and span, sp = ' + str(sp) + \
                      ' yields no solution for decreasing x-values and the delta-y value is a constant for (x0 - sp) < x <= (x0 + sp).')
                print('The 2 lines are therefore parallel and they never intersect each other in Euclidean space.')
                PL = True
        
            else :
                print(str(a) + ' != ' + str(c))
                print('But the delta-y value is a constant for x >= (x0 - sp).')
                print('The x-value which you have initiated earlier is the x-value of the point of intersection itself!')
                print('The solution is x = ' + str(x0) + '.')
                PE = True
            break
                
        elif y1 == y2 :
            x = x + dx
            print('Delta y converges for decreasing x-values.\nThe solution is x = ' + str(x) + '.')
            PDS = True
            xPDS = str(x)
            break

    if (y1 != y2) and ((y2 - y1) != (y02 - y01)) :
            
        if abs(y2 - y1) > abs(y02 - y01):
            print('Iterations with initiated x-value = ' + str(x0) + ' step size dx = ' + str(dx) +  ' , and span, sp = ' + str(sp) + \
                  ' yields no solution and delta y diverges with decreasing values of x.')
            PD = False
            
        elif abs(y2 - y1) < abs(y02 - y01) :
            print('Iterations with initiated x-value = '+ str(x0) + ' step size dx = ' + str(dx) + ' , and span, sp = ' + str(sp) + \
                  ' yields no solution and delta y converges with decreasing values of x.')
            PD = True
        else:
            print('Program error. Please kindly report the bug to the author. Thanks!')

    if (PE == True):
        print()
        print('Conclusion: The solution is x = ' + str(x0) + '.')

    elif (PL == True):
        if (a == c) and (b != d):
            print()
            print("Conclusion: The 2 lines are parallel. They never intersect each other in Euclidean space. There is no solution.")
        else:
            print()
            print("Conclusion: The 2 lines are exactly the same! They have infinitely many solutions.")

    elif ((PIS == True) and (PD == False)):
        print()
        print('Conclusion: Solution converges for increasing x-values. The solution is x = ' + xPIS + '.')

    elif ((PDS == True) and (PI == False)):
        print()
        print('Conclusion: Solution converges for decreasing x-values. The solution is x = ' + xPDS + '.')

    elif ((PI == True) and (PD == False)):
        print()
        print('Conclusion: No solution is found, but as delta y converges with increasing values of x, this is a strong hint that the solution is at x > x0.\nTry increasing the span, sp or increasing your initial x-value, x0.')
        print('Also take note too large a dx value can cause the solver to miss the solution altogether, try reducing your dx value as well if everything else fail.')
    elif ((PI == False) and (PD == True)):
        print()
        print('Conclusion: No solution is found, but as delta y converges with decreasing values of x, this is a strong hint that the solution is at x < x0.\nTry increasing the span, sp or decreasing your initial x-value, x0.')
        print('Also take note too large a dx value can cause the solver to miss the solution altogether, try reducing your dx value as well if everything else fail.')
    elif ((PI == False) and (PD == False)):
        print()
        print('Conclusion: There is a solution in between (x0 - sp) and (xo + sp), but your step size is too large, and the solver miss the solution altogether.')
        print('Reduce your step size!')

    confirm_input = 'Try Again'
    while confirm_input == 'Try Again':
        print()
        print('Thanks for trying out the program. Would you like to try the program again with other values.? Y/N')

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

try:  
    a = float(input('Enter a: '))  # input value for a and convert to float
    b = float(input('Enter b: '))  # input value for b and convert to float
    c = float(input('Enter c: '))  # input value for c and convert to float
except ValueError:  # catch errors if input cannot be converted to float
    print('Error! Enter a number.')  # an error message for invalid input

D = b ** 2 - 4 * a * c  # calculate the discriminant
try:  
    if D < 0:  # if the discriminant is less than 0
        print('The quadratic equation has no real roots.')  
    elif D == 0:  # if the discriminant is 0
        x = -b / (2 * a)  # calculation of the root
        print(f'The quadratic equation has one root: x = {x}')  # display the root
    else:  # if the discriminant is greater than 0
        x1 = (-b - D ** 0.5) / (2 * a)  # calculation of the first root
        x2 = (-b + D ** 0.5) / (2 * a)  # calculation of the second root
        print(f'The quadratic equation has two roots: x1 = {x1}, x2 = {x2}')  # display the roots
except ZeroDivisionError:  # catch errors if there is division by zero
    print('Error! Division by zero.')  # an error message for division by zero








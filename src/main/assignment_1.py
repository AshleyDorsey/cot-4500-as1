# import libraries as necessary

import decimal
import numpy as np
import math

# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
#       a) 0 | 10000000111 | 1110101110010000000000000000000000000000000000000000
# formula to use: (-1)^s*2^c-1027*(1 + f)

# this function will actually be used for questions 1 - 4 because the same numbers are used.
def binary_double_precision():
    
    # calculating the sign (s)
    s = 0
    # print(s) - used for testing

    # calculating the exponent (c)
    exponent = 10000000111
    c = 0
    iteration = 0

    # use a while loop to determine what the exponent portion of the binary would be (true calculations).
    while(exponent != 0):
        exp = exponent % 10
        c = c + exp * pow(2, iteration)
        exponent = exponent // 10
        iteration += 1
    # print(c) - used for testing

    # calculating the fraction (f)
    binary_fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    iteration = 1

    # use a for loop to go through the string of the fraction to calculate the f.
    for item in binary_fraction:
        f = f + int(item) * ((1/2)**iteration)
        iteration += 1
    # print(f) - used for testing

    # formula for converting binary to decimal (n)
    n = ((-1)**s)*(2**(c - 1023))*(1 + f)
    # use rounding to get to the answer desired: 491.5625
    print(f"{n:.4f}")
    print("\n")

    # Question 2: Repeat question 1 using three-digit chopping arithmetic
    
    # multiply by 10^-3 to get decimals.
    # use the math.floor function to get the rounded down version. Multiply by 1000 so that it keeps the desired numbers.
    #n = n * 10**-3
    print(float(math.floor(n)))
    print("\n")
    
    #Question 3: Repeat question 1 using three-digit rounding arithmetic
    
    # add .0005 to follow the rounding process.
    n = n + 0.0005
    # round this to 3 digits, it will round to what is necessary.
    print(float(round(n)))
    print("\n")
    
    # Question 4: Compute the absolute and relative error with the exact value form question 1 and its 3 digit rounding

    # function to get the absolute error value. Use the decimal library to print out the right amount of decimal places.
    def abs_err(n, n_bar):
        return abs((decimal.Decimal(n)) - (decimal.Decimal(n_bar)))
    
    # function to get the relative error value.
    def rel_err(n, n_bar):
        if n == 0:
            return 0
        else:
            return ((abs_err(n, n_bar)) / abs(decimal.Decimal(n)))
    
    # function to define values and print final error values.
    def absolute_and_relative_error():
        # redefine n because it is not defined within these functions, and because it was changed a lot...
        n = ((-1)**s)*(2**(c-1023))*(1 + f)
        # create the approximated value again (same as question 3)
        round_round = round(n)
        print(abs_err(n, round_round))
        print(rel_err(n, round_round))
        return

    # call final function so it will print the values in output.
    absolute_and_relative_error()
    print("\n")

# Question 5: What is the minimum number of terms needed to computer f(1) with error <10^-4? 

def series_error():
    # create the function that goes through the series.
    def infinite_series(x, k: int):
        return ((-1)**k) * ((x**k) / (k**3))
    
    # set the minimum error so we can compare later.
    minimum_error = .0001
    # we are looking for iterations! This is important! You can't set this equal to 0 because you can't divide by 0, so set equal to
    # 1 and fix later.
    iteration_counter = 1

    # create a while loop for as long as the function above is greater than the minimum error.
    while(abs(infinite_series(1, iteration_counter)) > minimum_error):
        # keep adding to the iterations.
        iteration_counter += 1

    # this is the fix...subtract the original 1.
    iteration_counter = iteration_counter - 1
    print(iteration_counter) 

# Question 6: Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0 with accuracy 10^-4 
# using a = -4 and b = 7.
#       b) Using the bisection method
#       c) Using the newton Raphson method - should be 37

# function for bisection method using the range which is defined in main function.
def bisection_method(a: int, b: int, tolerance: float):
    # subtract b from a.
    y = b - a
    # create a log base 10 of the subtraction from above.
    x = math.log(y, 10)
    # create a log base 10 of the tolerance.
    z = math.log(tolerance, 10)
    # subtract the above logs from each other and then divide by log base 10 of 2.
    equation = (x - z) / (math.log(2, 10))
    # round up because you can't have half of an iteration.
    print(math.ceil(equation))

# function for newton raphson method using the function, derivative, initial approximation, and tolerance.
def newton_raphson_method(funct, funct_deriv, initial_approximation, tolerance):
    # set up the equation to get the roots. 
    final_equation_necessary = funct(initial_approximation) / funct_deriv(initial_approximation)
    #set x = to initial approximation.
    x = initial_approximation

    # set iteration count equal to 1
    iteration_count = 1
    
    # create a while loop for as long as the final equation is greater than or equal to the tolerance.
    while(abs(final_equation_necessary) >= tolerance):
        # set x equal to the initial approximation minus the answer from the final equation.
        x = x - final_equation_necessary
        # add to the iteration count.
        iteration_count += 1
        # reset the final equation to be the function divided by the derivative.
        final_equation_necessary = funct(x) / funct_deriv(x)

    # return the iteration count.
    return iteration_count

# the main function
if __name__ == "__main__":
    # questions 1 - 4: question 4 needs some help
    binary_double_precision()

    #question 5:
    series_error()
    print("\n")

    #question 6:

    # (a) bisection method
    # set the range
    a = -2 # (also left)
    b = 5  # (also right)
    # set the tolerance
    tolerance: float = .0001
    bisection_method(a, b, tolerance)
    print("\n")

    # (b) newton raphson method - getting a WAY too big number
    # set the initial approximation
    initial_approximation: float = 7
    # set the tolerance
    tolerance: float = .0001
    # set up the function
    function_of_x = lambda x: (x**3) + (4*(x**2)) - 10
    # set up the derivative
    derivative_of_function_x = lambda x: (3*(x**2)) + 8*x
    print(newton_raphson_method(function_of_x, derivative_of_function_x, initial_approximation, tolerance))
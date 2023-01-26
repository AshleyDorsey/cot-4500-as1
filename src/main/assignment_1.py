import numpy as np
import math

# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
#       a) 0 | 10000000111 | 1110101110010000000000000000000000000000000000000000
# formula to use: (-1)^s*2^c-1027*(1 + f)

def binary_double_precision():
    # calculating the sign (s)
    s = 0
    # print(s)

    # calculating the exponent (c)
    exponent = 10000000111
    c = 0
    i = 0
    while(exponent != 0):
        exp = exponent % 10
        c = c + exp * pow(2, i)
        exponent = exponent // 10
        i += 1
    # print(c)

    # calculating the fraction (f)
    binary_fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    i = 1
    for item in binary_fraction:
        f = f + int(item) * ((1/2)**i)
        i += 1
    # print(f)

    # formula for converting binary to decimal (n)
    n = ((-1)**s)*(2**(c - 1023))*(1 + f)
    print(f"{n:.5f}")
    print("\n")

    # Question 2: Repeat question 1 using three-digit chopping arithmetic
    
    n = n * (10**-3)
    print((math.floor(n * 1000))/1000)
    print("\n")
    
    #Question 3: Repeat question 1 using three-digit rounding arithmetic
    
    n = n + 0.0005
    print(round(n, ndigits = 3))
    print("\n")
    
    # Question 4: Compute the absolute and relative error with the exact value form question 1 and its 3 digit rounding

    # redefine n because I changed it for questions 2 and 3:

    def abs_err(n, n_bar):
        return abs(n - n_bar)
    
    def rel_err(n, n_bar):
        if n == 0:
            return 0
        else:
            return ((abs_err(n, n_bar)) / abs(n))
    
    def absolute_and_relative_error():
        n = ((-1)**s)*(2**(c-1023))*(1 + f)
        round_round = round(n, ndigits = 3)
        print(abs_err(n, round_round))
        print(rel_err(n, round_round))
        return

    absolute_and_relative_error()
    print("\n")

# Question 5: What is the minimum number of terms needed to computer f(1) with error <10^-4? 

def series_error():
    def infinite_series(x, k: int):
        return ((-1)**k) * ((x**k) / (k**3))
    
    minimum_error = 1e-4
    iteration_counter = 1

    while(abs(infinite_series(1, iteration_counter)) > minimum_error):
        iteration_counter += 1

    iteration_counter = iteration_counter - 1
    print(iteration_counter) 

# Question 6: Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0 with accuracy 10^-4 
# using a = -4 and b = 7.
#       b) Using the bisection method
#       c) Using the newton Raphson method - should be 37


def bisection_method(a: int, b: int, tolerance: float):
    y = b - a
    x = math.log(y, 10)
    z = math.log(tolerance, 10)
    equation = (x - z) / (math.log(2, 10))
    print(math.ceil(equation))

def newton_raphson_method(funct, funct_deriv, initial_approximation, tolerance):
    answer = funct(initial_approximation) / funct_deriv(initial_approximation)
    x = initial_approximation

    iteration_count = 1
    
    while(abs(answer) >= tolerance):
        x = x - answer
        iteration_count += 1
        answer = funct(x) / funct_deriv(x)

    return iteration_count


if __name__ == "__main__":
    # questions 1 - 4: question 4 needs some help
    binary_double_precision()

    #question 5:
    series_error()
    print("\n")

    #question 6:

    # (a) bisection method
    a = -2 # (also left)
    b = 5  # (also right)
    tolerance: float = 10**-4
    bisection_method(a, b, tolerance)
    print("\n")

    # (b) newton raphson method - getting a WAY too big number
    initial_approximation: float = 7
    tolerance: float = .0001
    function_of_x = lambda x: (x**3) + (4*(x**2)) - 10
    derivative_of_function_x = lambda x: (3*(x**2)) + 8*x
    print(newton_raphson_method(function_of_x, derivative_of_function_x, initial_approximation, tolerance))
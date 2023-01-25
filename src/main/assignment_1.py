import numpy as np
import math

# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
#       a) 0 | 10000000111 | 1110101110010000000000000000000000000000000000000000
# formula to use: (-1)^s*2^c-1027*(1 + f)

def double_precision():
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
    n = ((-1)**s)*(2**(c-1023))*(1 + f)

    def absolute_error(value: float, y: int):
        return (abs(value - round(value, ndigits =y)))
    
    print(absolute_error(n, 3))
    print("\n")
    
    def relative_error(value: float, y: int):
        return(abs(value - round(value, ndigits = y))) / (abs(value))

    print(relative_error(n, 3))
    print("\n")

# Question 5: What is the minimum number of terms needed to computer f(1) with error <10^-4?

def series_error():
    def infinite_series(x, k: int):
        return ((-1)**k) * ((x**k) / (k**3))
    
    minimum_error = 1e-4
    iteration_counter = 1

    while(abs(infinite_series(1, iteration_counter)) > minimum_error):
        iteration_counter += 1

    print(iteration_counter)

# Question 6: Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0 with accuracy 10^-4 
# using a = -4 and b = 7.
#       b) Using the bisection method
#       c) Using the newton Raphson method


# CONTINUE WORKING ON THIS -- DEFINITELY NOT RIGHT!!!!!

def bisection_method(left: float, right: float, function_string):
    x = left
    initial_left = eval(function_string)
    x = right
    initial_right = eval(function_string)

    if initial_left * initial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    
    tolerance: float = .001
    difference: float = right - left

    while(difference >= tolerance):

        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(function_string)
        
        if evaluated_midpoint == 0.0:
            break
    
        x = left
        evaluated_left_point = eval(function_string)

        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional == True:
            right = mid_point
        else:
            left = mid_point

        difference = abs(right - left)
        print(difference)

def func(x):
    return x*x*x - 4*x*x - 10

def bisect(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = (a + b) / 2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisect(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisect(f, a, m, tol)
    
def my_newton(f, df, x0, tol):
    if abs(f(x0)) < tol:
        return x0
    else:
        ...
f = lambda x: x*x*x - 4*x*x - 10
f_prime = lambda x: 3*x*x - 8*x       
        

if __name__ == "__main__":
    # questions 1 - 4:
    double_precision()

    #question 5:
    series_error()
    print("\n")

    #question 6:

    # (a) bisection method
    left = -2
    right = 5
    function_string = "(x**3) - (4*(x**2)) - 10"
    #bisection_method(left, right, function_string)

    # (b) newton raphson method
    #print(bisect(f, -4, 7, .001))
    #print()
    #print(my_newton(f, f_prime, 7, .001))
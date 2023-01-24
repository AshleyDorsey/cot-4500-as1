import numpy as np
import math

# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
#       a) 0 | 10000000111 | 1110101110010000000000000000000000000000000000000000
# formula to use: (-1)^s*2^c-1027*(1 + f)

def binary_double_precision():
    # calculating the sign (s)
    binary_s = 0
    print(binary_s)

    # calculating the exponent (c)
    binary_exponent = 10000000111
    c = 0
    i = 0
    while(binary_exponent != 0):
        exp = binary_exponent % 10
        c = c + exp * pow(2, i)
        exponent = binary_exponent // 10
        i += 1
    print(c)

    # calculating the fraction (f)
    binary_fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    i = 1
    for item in binary_fraction:
        f = f + int(item) * ((1/2)**i)
        i += 1
    print(f)

    # formula for converting binary to decimal (n)
    n = ((-1)**binary_s)*(2**(c - 1023))*(1 + f)
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

def bisection_method(left: float, right: float, function_string: str):
    x = left
    initial_left = eval(function_string)
    x = right
    initial_right = eval(function_string)

    if initial_left * initial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .001
    difference: float = right - left

    max_iterations: int = 20 # change later - this is just for now
    iteration_counter: int = 0
    function_a = "x**3 + 4*x**2 - 10"
    while(difference >= tolerance and iteration_counter <= max_iterations):
        iteration_counter += 1
        
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(function_string)

        if evaluated_midpoint == 0.0:
            break

        x = left
        evaluated_left_point = eval(function_string)

        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

def custom_derivative(value):
    return(3 * value * value) - (8 * value) # should be right - check with others

def newton_raphson_method(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f'
    f_prime = custom_derivative(initial_approximation)

    function_over_derivative: float = f / f_prime
    while(abs(function_over_derivative) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f'
        f_prime = custom_derivative(initial_approximation)

        # division operation
        function_over_derivative = f / f_prime

        # subtraction operation
        initial_approximation -= function_over_derivative
        iteration_counter += 1

    print(f"The iteration {iteration_counter} has an error threshold of: {function_over_derivative}")
    print(iteration_counter)

if __name__ == "__main__":
    # question 1 - 4:
    binary_double_precision()

    #question 5:
    series_error()
    print("\n")

    # question 6:
    left = -4
    right = 7
    function_string = "(x**3) - (4*(x**2)) - 10"
    bisection_method(left, right, function_string)
    
    initial_approximation: float = -4 # what does this need to be?
    tolerance: float = .001
    sequence: str = "(x**3) + 4*(x**2) - 10"
    #print(newton_raphson_method(initial_approximation, tolerance, sequence))
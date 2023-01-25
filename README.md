# cot-4500-as1
 
#### By **Ashley Dorsey**

#### Assignment covering topics from chapters 1 and 2.

## Technologies Used

- GitHub

- Python

## Description

Question 1, 2, 3, and 4 go hand in hand. The first question converts a 64 bit binary number into a decimal by calculating each part of the binary number: sign, exponent, and fraction. This answer is used for the next three problems. For question 2, the answer is a three-digit decimal that is "chopped" meaning that it is not rounded to the nearest whole number, simply that the digits after the one specified are removed. The third question does the rounding, or adds .0005 and rounds to the nearest thousandth's place after that. The fourth and final question involved in this uses the decimal from question 1 to determine the absolute and relative error. For absolute error, you take the answer from question 1 and subtract from it a rounded version of the same number and then take the absolute value of that. For relative error, you take the answer from the absolute error and divide by the absolute value of the answer from question 1.

Question 5 is the first to deviate. We are looking for the minimum number of terms needed in order for a specific series to have an error less than .001. 

Question 6 has two parts, both of which are used to determine the number of iterations necessary to compute a specific function with an accuracy of .001 and a range of -4 to 7. The first method is the bisection method, which uses both endpoints and the midpoint to determine the roots of the equation. The second method is the Newton-Raphson method, which uses approximations from the value and from the derivative to try and calculate the roots.

## Setup/Installation Requirements

- Create a requirements.txt. This can be done by typing into the terminal "pip freeze > requirements.txt".

- Install numpy by typing into the terminal "pip install numpy". However, if this is already installed, you may not need to install again.

- At the top of the program it is necessary to import both the "math" library and "numpy" for this.

- In the command line, enter "python assignment_1.py" and then hit ENTER to run.
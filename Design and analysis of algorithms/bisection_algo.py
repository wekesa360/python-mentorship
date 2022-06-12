"""
 Write a program using bisection method algorithm to find the root of a quadratic equation.
"""

        # For a given function f(x),the Bisection Method algorithm works as follows:

        #     1. two values a and b are chosen for which f(a) > 0 and f(b) < 0 (or the other way around)
        #     2. interval halving: a midpoint c is calculated as the arithmetic mean between a and b, c = (a + b) / 2
        #     3. the function f is evaluated for the value of c
        #     4. if f(c) = 0 means that we found the root of the function, which is c
        #     5. if f(c) ≠ 0 we check the sign of f(c):
        #         1. if f(c) has the same sign as f(a) we replace a with c and we keep the same value for b
        #         2. if f(c) has the same sign as f(b), we replace b with c and we keep the same value for a
        #     6. we go back to step 2. and recalculate c with the new value of a or b

        # The algorithm ends when the values of f(c) is less than a defined tolerance (e.g. 0.001). 
        # In this case we say that c is close enough to be the root of the function for which f(c) ~= 0.
        # In order to avoid too many iterations, we can set a maximum number of iterations (e.g. 1000) and even if we are above the defined tolerance, 
        # we keep the last value of c as the root of our function.

        # Source: (https://x-engineer.org/bisection-method/)

from datetime import datetime

def get_input():
    """
    Takes is user input from stdin.
    Return: an array of user inputs
    """
    a = int(input("Enter a number, a: "))
    b = int(input("Enter a number, b: "))
    N = int(input("Enter number of maximum iterations: "))
    TOL = float(input("Enter tolerance: "))
    output = [ a, b, N, TOL]
    return output

def bisection_algo(f,a, b, N, TOL):
    """
   Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters:
        f : function
            The function for which we are trying to approximate a solution f(x)=0.
        a,b : numbers(integers)
            The interval in which to search for a solution. The function returns
            None if f(a)*f(b) >= 0 since a solution is not guaranteed.
        N : (positive) integer
        TOL : (positive) number - defined tolerance
    
    Return: root
    """

    def sign(x):
        """
        check sign of a number 
        parameters:
            x : number
        return: 1 if x is positive, -1 if x is negative, 0 if x is zero
        """
        return 1 if x >= 0 else -1
    if (sign(f(a)) == sign(f(b))):
        return "Invalid input"
    c = (a + b) / 2
    for i in range(N):
        if f(c) == 0:
            return c
        if TOL <= abs(f(c)):
            if sign(f(c)) == sign(f(a)):
                a = c
            if sign(f(c)) == sign(f(b)):
                b = c
            c = (a + b) / 2
            # print("{} => {} and f(c) = {}".format(i, c, f(c)))
    return c

if '__main__' == __name__:
    output = get_input()
    f = lambda x: 10 - x**2
    print("#############################################")
    init_time = datetime.now()
    print(bisection_algo(f, output[0], output[1], output[2], output[3]))
    end_time = datetime.now()
    print("Time taken : ", end_time - init_time)
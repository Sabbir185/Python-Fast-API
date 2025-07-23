"""
Positional arguments
"""
def doSum(a, b):
    print("I am printing the sum of two numbers")
    return a+b

print(doSum(5, 10))


def multiFunc(name, dept):
    print(f"My name is {name}, {dept} department.")
    return None

multiFunc("Alice", "Engineering")


"""
Keyword arguments
"""
def doSumKeyword(a, b):
    print(f"{b} - {a} = {b - a}")

doSumKeyword(b=15, a=10)


"""
Default or optional arguments or parameters
"""
def country(name="Bangladesh"):
    print(f"My country is {name.upper()}")
    
country() # optional argument

"""
Variable length arguments --> *args and **kwargs
*args -> make an tuple of arguments
**kwargs -> make a dictionary of keyword arguments
"""
def variableLengthArgs(*args):
    print(args)

variableLengthArgs(1, 2, 3, 4, 5)

def variableLengthKeywordArgs(**kwargs):
    print(kwargs)

variableLengthKeywordArgs(name="Alice", age=30, city="New York")


"""
Returning multiple values from a function
"""
def doMathOperations(a, b):
    return a + b, a - b, a * b, a / b

sum, diff, prod, quot = doMathOperations(10, 5)
print(f"Sum: {sum}, Difference: {diff}, Product: {prod}, Quotient: {quot}")


"""
Recursion
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(f"Factorial of 5: {factorial(5)}")


"""
Excute runtime
"""
x = 0
if x:
    def hello():
        print('Hello, World!')
else:
    def hello():
        print('Hello, Universe!')

hello()
# Prints Hello, Universe!



def findSqure(x):
    return x ** 2

def findCube(x):
    return x**3

exponent = {"squre": findSqure, "cube": findCube}

print(exponent["squre"](3))
print(exponent["cube"](3))


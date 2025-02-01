# app.py - A simple calculator app with more functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def square(a):
    return a*a

if __name__ == "__main__":
    print("Sum:", add(5, 3))
    print("Difference:", subtract(5, 3))
    print("Product:", multiply(5, 3))

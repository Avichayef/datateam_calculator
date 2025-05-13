class Calculator:
    """
    A simple calculator for basic arithmetic operations
    """
    
    def add(self, a, b):
        #Addition
        return a + b
    
    def subtract(self, a, b):
        #Subtraction
        return a - b
    
    def multiply(self, a, b):
        #Multiplication
        return a * b
    
    def divide(self, a, b):
        #Division
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
from app.calculator import Calculator


if __name__ == "__main__":
    calc = Calculator()
    
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Operation: [+, -, *, /]")

    try:
        if op == "+":
            result = calc.add(a, b)
        elif op == "-":
            result = calc.subtract(a, b)
        elif op == "*":
            result = calc.multiply(a, b)
        elif op == "/":
            result = calc.divide(a, b)
        else:
            raise ValueError("Unknown operation")

        print(f"Result: {result}")
    except Exception as e:
        print("Error:", e)

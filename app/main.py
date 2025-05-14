"""
Calculator Web App
"""

from flask import Flask, request, jsonify, render_template
from app.calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/api')
def api_info():
    return jsonify({
        "message": "Calculator API",
        "endpoints": {
            "/": "Web interface",
            "/api": "API information",
            "/health": "Health check endpoint",
            "/calculate": "POST endpoint for calculations"
        }
    })

@app.route('/health')
def health():
    """
    Health check endpoint for monitoring application status.
    
    """
    return jsonify({"status": "healthy"})

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Perform mathematical calculations based on JSON input.

    """
    try:
        # Validate input
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data provided")
            
        # Extract and validate operands
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        operation = data.get('operation')

        if not operation:
            raise ValueError("No operation specified")

        # Perform calculation based on operation
        if operation == "+":
            result = calc.add(a, b)
        elif operation == "-":
            result = calc.subtract(a, b)
        elif operation == "*":
            result = calc.multiply(a, b)
        elif operation == "/":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            result = calc.divide(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")

        # Return successful result
        return jsonify({
            "operation": operation,
            "a": a,
            "b": b,
            "result": result
        })
    except Exception as e:
        # Return error response
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
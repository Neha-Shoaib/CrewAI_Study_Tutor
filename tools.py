from crewai.tools import tool

@tool("CalculatorTool")
def calculate_expression(expression: str) -> str:
    """Useful to calculate mathematical expressions accurately. 
    Input should be a clean math string, e.g., '15 * 12 + 45' or '100 / 4'."""
    try:
        # Safe evaluation restricted to standard arithmetic
        allowed = set("0123456789+-*/(). %")
        if not all(c in allowed for c in expression):
            return "Invalid expression. Use basic numbers and arithmetic symbols."
        result = eval(expression, {"__builtins__": None}, {})
        return f"Calculation Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

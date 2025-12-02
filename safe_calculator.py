# safe_calculator.py
from simpleeval import simple_eval, SimpleEval, FunctionNotDefined, InvalidExpression

def main():
    print("Safe Calculator — type 'exit' to quit.")

    se = SimpleEval()
    # Optionally, you can restrict or extend allowed functions/operators here:
    # For example, you might disable power operator or disable certain functions.
    # By default simpleeval supports +, -, *, /, **, %, //, parentheses, and basic precedence.

    while True:
        expr = input("Enter an expression: ").strip()
        if expr.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break

        try:
            result = se.eval(expr)
            print("Result:", result)
        except (FunctionNotDefined, InvalidExpression, ZeroDivisionError) as e:
            print("Error: Invalid expression or operation —", e)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

def eval_postfix(expression):
    stack = []
    
    # Define operations using lambda functions for cleanliness
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        # Using integer division '//' to match standard RPN integer problems. 
        # For floating-point division, use: a / b
        '/': lambda a, b: int(a / b)  
    }
    
    for token in expression:
        if token in operations:
            # Pop operands in reverse order
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Perform the calculation
            result = operations[token](operand1, operand2)
            stack.append(result)
        else:
            # Token is a number, cast it to int and push to stack
            stack.append(int(token))
            
    return stack[0]

# --- Testing the Example ---
expr = ['2', '1', '+', '3', '*']
print(f"Result of {expr} is: {eval_postfix(expr)}") # Output: 9
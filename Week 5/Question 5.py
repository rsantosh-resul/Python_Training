def infix_to_postfix(expression: str) -> str:
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    stack = []      # Holds operators and parentheses
    output = []     # Holds the final postfix tokens
    
    # Split the string into tokens (handles spacing safely)
    tokens = expression.split()
    
    for token in tokens:
        # Case 1: If token is alphanumeric (operand), add to output
        if token.isalnum():
            output.append(token)
            
        # Case 2: Left parenthesis goes straight to stack
        elif token == '(':
            stack.append(token)
            
        # Case 3: Right parenthesis clears the stack until a '(' is found
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the '(' from the stack
            
        # Case 4: Operator encountered
        elif token in precedence:
            while (stack and stack[-1] in precedence and 
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
            
    # Pop all remaining operators from the stack
    while stack:
        output.append(stack.pop())
        
    return " ".join(output)

# --- Running the Example ---
infix_expr = "3 + 4 * 2"
postfix_expr = infix_to_postfix(infix_expr)

print(f"Infix:   '{infix_expr}'")
print(f"Postfix: '{postfix_expr}'")  # Output: '3 4 2 * +'
def validate_stack_sequences(pushed, popped):
    stack = []
    pop_idx = 0  # Pointer to track our progress through the popped sequence
    
    for val in pushed:
        stack.append(val)  # Simulate a push operation
        
        # Look ahead: as long as the top of our stack matches the expected 
        # popped element, we simulate a pop operation.
        while stack and stack[-1] == popped[pop_idx]:
            stack.pop()
            pop_idx += 1  # Move to the next expected popped element
            
    # If the stack is empty, every pushed element was successfully and validly popped
    return len(stack) == 0

# --- Running the Example ---
pushed_seq = [1, 2, 3, 4, 5]
popped_seq = [4, 5, 3, 2, 1]

is_valid = validate_stack_sequences(pushed_seq, popped_seq)
print(f"Is the stack sequence valid? {is_valid}")  # Expected Output: True
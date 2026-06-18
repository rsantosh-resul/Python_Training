class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        # Only push to min_stack if it's empty or val is a new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.main_stack:
            return
        # If the value being removed is the minimum, pop it from min_stack too
        if self.main_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1] if self.main_stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

    def print_state(self, operation):
        """Helper to visualize stack states"""
        print(f"After {operation[0]:12} -> Main Stack: {self.main_stack[0]:<15} | Min Stack: {self.min_stack[0]:<10} | Current Min: {self.getMin()}")


# --- Execution Example ---
if __name__ == "__main__":
    stack = MinStack()
    print("--- PUSH OPERATIONS ---")
    
    stack.push(10)
    stack.print_state("push(10)")
    
    stack.push(20)
    stack.print_state("push(20)") # 20 is larger than 10, min_stack won't change
    
    stack.push(5)
    stack.print_state("push(5)")  # 5 is a new minimum
    
    stack.push(5)
    stack.print_state("push(5)")  # Duplicate minimum is tracked correctly
    
    print("\n--- POP & GETMIN OPERATIONS ---")
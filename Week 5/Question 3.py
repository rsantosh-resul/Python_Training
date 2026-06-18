class QueueWithStacks:
    def __init__(self):
        # in_stack handles all incoming elements (enqueue)
        self.in_stack = []
        # out_stack handles all outgoing elements (dequeue/peek)
        self.out_stack = []

    def enqueue(self, val: int) -> None:
        """Add an element to the end of the queue."""
        self.in_stack.append(val)

    def _transfer_if_needed(self):
        """Private helper to move elements from in_stack to out_stack 
        only when out_stack runs out of elements."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self) -> int:
        """Remove and return the element from the front of the queue."""
        if self.empty():
            raise IndexError("Cannot dequeue from an empty queue")
            
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Get the front element without removing it."""
        if self.empty():
            raise IndexError("Cannot peek from an empty queue")
            
        self._transfer_if_needed()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Returns True if the queue is completely empty."""
        return not self.in_stack and not self.out_stack

    def print_state(self, action_name):
        """Helper method to print the internal stacks for debugging"""
        print(f"Action: {action_name:<15} | In-Stack: {str(self.in_stack):<12} | Out-Stack: {str(self.out_stack):<12}")

# --- Execution Example ---
if __name__ == "__main__":
    # Initialize our queue
    q = QueueWithStacks()
    print("--- Test 1: Enqueueing 3 items ---")
    q.enqueue(1)
    q.print_state("enqueue(1)")
    q.enqueue(2)
    q.print_state("enqueue(2)")
    q.enqueue(3)
    q.print_state("enqueue(3)")

    print("\n--- Test 2: First Dequeue (Triggers the internal transfer) ---")
    # This peek/dequeue forces the items to invert into out_stack
    print(f"Current Front (peek): {q.peek()}")
    popped_val = q.dequeue()
    print(f"Dequeued value: {popped_val}")
    q.print_state("dequeue()")

    print("\n--- Test 3: Enqueueing another item while out_stack has elements ---")
    q.enqueue(4)
    q.print_state("enqueue(4)")

    print("\n--- Test 4: Emptying the remaining Queue ---")
    while not q.empty():
        print(f"Dequeued value: {q.dequeue()}")
        q.print_state("dequeue()")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    """
    Returns True if a cycle exists in the linked list, 
    otherwise returns False.
    """
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        # If they meet, a cycle has been detected!
        if slow == fast:
            return True
            
    return False  # Fast pointer reached the end, so no cycle exists

# --- Testing the Algorithm ---
if __name__ == "__main__":
    # 1. Create nodes: 1 -> 2 -> 3 -> 4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    print(f"Before creating loop : {has_cycle(node1)}") # Expected: False
    
    # 2. Introduce a cycle: Connect 4 back to 2 (4 -> 2)
    # The chain is now: 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 ...
    node4.next = node2
    
    print(f"After creating loop : {has_cycle(node1)}")  # Expected: True
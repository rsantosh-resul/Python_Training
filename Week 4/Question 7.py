class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_cycle_start(head):
    if not head or not head.next:
        return None
        
    slow = head
    fast = head
    
    # --- Phase 1: Find if a cycle exists ---
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break  # Pointers collided, cycle confirmed!
    else:
        return None  # Loop exited normally, meaning no cycle exists
        
    # --- Phase 2: Find the entrance of the cycle ---
    slow = head  # Reset slow to the beginning
    
    # Move both pointers 1 step at a time until they meet again
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow  # Or fast, since they are pointing to the exact same starting node

# --- Testing the Algorithm ---
if __name__ == "__main__":
    # Constructing: 1 -> 2 -> 3 -> 4 -> 5
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    # Creating a cycle: Link 5 back to 3
    # 1 -> 2 -> [3 -> 4 -> 5 -> back to 3]
    node5.next = node3
    
    start_node = detect_cycle_start(node1)
    if start_node:
        print(f"Cycle begins at node with value: {start_node.data}")  # Expected: 3
    else:
        print("No cycle detected.")
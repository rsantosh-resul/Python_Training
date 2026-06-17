class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def remove_nth_from_end(head, n):
    # Create a dummy node that sits right before the head
    dummy = Node(0)
    dummy.next = head
    
    fast = dummy
    slow = dummy
    
    # Step 1: Move the fast pointer forward so there is a gap of n nodes 
    # between slow and fast (advancing n + 1 times total from dummy)
    for _ in range(n + 1):
        fast = fast.next
        
    # Step 2: Move both pointers together until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
        
    # Step 3: slow is now pointing to the node BEFORE the one to be deleted.
    # Stitch the pointers to skip the target node.
    slow.next = slow.next.next
    
    # Return the real head of the modified list
    return dummy.next

def print_list(head):
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements) + " -> None")

if __name__ == "__main__":
    # Constructing: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original List:")
    print_list(head)

    # Remove 2nd node from the end (Node 4)
    head = remove_nth_from_end(head, n=2)

    print("\nModified List:")
    print_list(head)
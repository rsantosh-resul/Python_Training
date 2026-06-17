class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    # Create a dummy node to act as the anchor
    dummy = Node()
    # The tail pointer will build our new list node-by-node
    tail = dummy
    
    # Loop until one of the lists runs out of nodes
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1  # Link the smaller node
            l1 = l1.next    # Move the pointer forward in list 1
        else:
            tail.next = l2  # Link the smaller node
            l2 = l2.next    # Move the pointer forward in list 2
            
        tail = tail.next    # Advance our merged list's tail
        
    # If there are remaining nodes in either list, append them to the end
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
        
    # The actual merged list starts right after the dummy node
    return dummy.next

# --- Testing the Algorithm ---
def print_list(head):
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements) + " -> None")

if __name__ == "__main__":
    # List 1: 1 -> 3 -> 5
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    # List 2: 2 -> 4 -> 6
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    print("List 1:")
    print_list(l1)
    print("List 2:")
    print_list(l2)

    merged_head = merge_sorted_lists(l1, l2)
    print("\nMerged Sorted List:")
    print_list(merged_head)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")
        
def reverse_linked_list(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  # 1. Bookmark the next node
        curr.next = prev       # 2. Reverse the pointer (point backward)
        prev = curr            # 3. Move 'prev' one step forward
        curr = next_node       # 4. Move 'curr' one step forward
        
    return prev  

# --- Running the Example ---
if __name__ == "__main__":
    # 1. Create a linked list: 1 -> 2 -> 3 -> 4 -> None
    ll = LinkedList()
    for value in [1, 2, 3, 4]:
        ll.append(value)

    # 2. Reverse the list and update the list's head reference
    ll.head = reverse_linked_list(ll.head)

    print("\nReversed List:")
    ll.print_list()
class Node:
    """A class to represent an individual node in the linked list."""
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None  # Pointer to the next node, initialized to None


class LinkedList:
    """A class to represent a Singly Linked List."""
    def __init__(self):
        self.head = None  # The list starts out empty, so head is None

    def append(self, data):
        """Add a new node with the given data to the END of the list."""
        new_node = Node(data)
        
        # Case 1: If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
            
        # Case 2: Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Link the last node's 'next' pointer to our new node
        current.next = new_node

    def prepend(self, data):
        """Add a new node with the given data to the BEGINNING of the list."""
        new_node = Node(data)
        
        # Point the new node's next pointer to the current head
        new_node.next = self.head
        
        # Move the head of the list to point to the new node
        self.head = new_node

    def delete_by_value(self, target_value):
        """Remove the first node that matches the target_value."""
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        # Case 1: The item to delete is the head node
        if self.head.data == target_value:
            self.head = self.head.next  # Bypass the old head node
            return

        # Case 2: The item is somewhere down the line
        current = self.head
        # Look ahead at the next node's data
        while current.next and current.next.data != target_value:
            current = current.next

        # If we found the target value, stitch the pointers to bypass it
        if current.next:
            current.next = current.next.next
        else:
            print(f"Value '{target_value}' not found in the list.")

    def search(self, target_value):
        """Search for a value in the list. Returns True if found, False otherwise."""
        current = self.head
        
        while current:
            if current.data == target_value:
                return True
            current = current.next  # Move to the next node
            
        return False

    def print_list(self):
        """Print the entire linked list in a readable format."""
        if not self.head:
            print("Empty List")
            return
            
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
            
        print(" -> ".join(elements) + " -> None")


# --- Demonstration / Testing ---
if __name__ == "__main__":
    ll = LinkedList()
    
    print("--- Testing Append & Prepend ---")
    ll.append(10)
    ll.append(20)
    ll.prepend(5)   # Inserts 5 at the front
    ll.append(30)
    ll.print_list()  # Expected: 5 -> 10 -> 20 -> 30 -> None

    print("\n--- Testing Search ---")
    print(f"Is 20 in the list? {ll.search(20)}")  # Expected: True
    print(f"Is 99 in the list? {ll.search(39)}")  # Expected: False

    print("\n--- Testing Delete By Value ---")
    ll.delete_by_value(20) # Deleting a middle element
    ll.print_list()        # Expected: 5 -> 10 -> 30 -> None
    
    ll.delete_by_value(5)  # Deleting the head element
    ll.print_list()        # Expected: 10 -> 30 -> None
    
    ll.delete_by_value(100) # Deleting non-existent element
class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def is_palindrome(head):
    if not head or not head.next:
        return True
        
    # Step 1: Find the middle of the list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Step 2: Reverse the second half of the list in place
    # 'slow' is currently pointing to the middle node
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    # Step 3: Compare the first half and reversed second half
    first_half = head
    second_half = prev  # 'prev' is the head of the reversed second half
    
    is_pal = True
    while second_half:  # Only need to check the second half
        if first_half.data != second_half.data:
            is_pal = False
            break
        first_half = first_half.next
        second_half = second_half.next
        
    # Optional Step 4: Restore the list structure (Good practice)
    # Re-reversing the second half puts the list back to its original state
    
    return is_pal
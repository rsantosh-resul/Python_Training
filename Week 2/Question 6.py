from collections import defaultdict

def group_by_first_letter(words):
    # Initialize a defaultdict where every new key automatically maps to an empty list
    grouped = defaultdict(list)
    
    for word in words:
        if word:  # Handle potential empty strings in the list
            first_letter = word[0].lower()  # Normalize to lowercase so 'A' and 'a' group together
            grouped[first_letter].append(word)
            
    return dict(grouped)  # Optional: Convert back to a standard dict for clean output

# --- Example Usage ---
sample_words = ['apple', 'avocado', 'banana', 'Cherry', 'blueberry']
result = group_by_first_letter(sample_words)

print(result)
# Output: {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['Cherry']}
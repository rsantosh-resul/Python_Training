from collections import Counter

def find_most_common_char(text):
    if not text:
        return None  # Handle empty string edge case
    
    # 1. Count frequencies of all characters
    char_counts = Counter(text)
    
    # 2. Get the single most common element
    # .most_common(1) returns a list like: [('a', 5)]
    most_common = char_counts.most_common(1)
    
    # 3. Extract the tuple from the list and return it
    return most_common[0]

# --- Example Usage ---
sample_string = "success"
character, count = find_most_common_char(sample_string)

print(f"The most character used is '{character}' = {count}.")
# Output: The most character used is 's' = 3.
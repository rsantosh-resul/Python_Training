def remove_duplicates_preserve_order(items):
    # dict.fromkeys() creates a dictionary with list items as keys, dropping duplicates.
    # list() converts those unique keys back into a clean list.
    return list(dict.fromkeys(items))

# --- Example Usage ---
raw_list = ['banana', 'apple', 'banana', 'avocado', 'apple', 'cherry']
clean_list = remove_duplicates_preserve_order(raw_list)

print(clean_list)
# Output: ['banana', 'apple', 'avocado', 'cherry']
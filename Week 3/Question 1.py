# Time for Python Code = 15 mins
# Space Complexity = 5 values of memory usage

def two_sum(nums, target):
    # Map to store: value -> index
    seen = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in the map, we found our pair!
        if complement in seen:
            return [seen[complement], index]
        
        # Otherwise, save the current number and its index to the map
        seen[num] = index
        
    return []  # Return empty list if no pair is found

# --- Example Usage ---
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(f"Indices: {result}")
# Output: Indices: [0, 1] (Since nums[0] + nums[1] == 9)
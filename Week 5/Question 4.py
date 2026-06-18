def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stores indices of the days
    
    for current_day_idx, current_temp in enumerate(temperatures):
        # Check if the current day is warmer than the day on top of our stack
        while stack and current_temp > temperatures[stack[-1]]:
            older_day_idx = stack.pop()
            # The number of days to wait is the difference between the indices
            result[older_day_idx] = current_day_idx - older_day_idx
            
        # Always push the current day's index onto the stack
        stack.append(current_day_idx)
        
    return result

# --- Running the Example ---
temps = [73, 74, 75, 71, 69, 72, 76, 73]
output = daily_temperatures(temps)

print(f"Temperatures: {temps}")
print(f"Days to wait: {output}")
# Expected Output: [1, 1, 4, 2, 1, 1, 0, 0]
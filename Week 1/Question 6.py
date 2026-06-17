def has_dup(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

print(has_dup([1,2,3,1]))
print(has_dup([1,2,6,4]))
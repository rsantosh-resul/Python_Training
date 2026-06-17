def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))
print(is_palindrome("madam12"))

# Time Complexity : O(n)
# As the string length n grows, the number of comparisons grows linearly.
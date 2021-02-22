def any7(nums):
    """Checks if any of the numbers in the list num are a 7. Returns a boolean."""
    for num in nums:
        if num == 7:
            return True
    
    return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))


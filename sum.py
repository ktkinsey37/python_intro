def sum_nums(nums):
    """Given list of numbers, returns the sum of those number by looping over list."""
    sum = 0
    for num in nums:
        sum = num + sum
    return sum


print("sum_nums returned", sum_nums([1, 2, 3, 4]))

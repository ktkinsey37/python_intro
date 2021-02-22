def in_range(nums, lowest, highest):
    """Accepts a list, nums, and lowest and highest numbers of a range.
    Compares all numbers in the list to make sure they are in the highest => lowest range.
    If a number is in the range, prints "num fits", else it does nothing"""
    for num in nums:
      if num >= lowest and num <= highest:
        print(f'{num}  fits')
    

    # YOUR CODE HERE


print(in_range([10, 20, 30, 40, 50], 15, 30))            

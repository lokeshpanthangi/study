# Problem 1: The Transaction Compression

# Scenario: You are building a transaction processing engine.
#  You receive a batch of transaction IDs, where 0 represents a failed/null transaction and any other integer is a valid ID.

# Requirement: We need to "compress" the batch for storage. Shift all 
# valid transactions to the front of the array without changing their original order.
# The failed transactions (0s) must be moved to the end of the array to be discarded later.

# Constraint: You must do this in-place (minimize memory usage).

# Input: [0, 101, 0, 204, 55]

# Expected Output: [101, 204, 55, 0, 0]


nums = [0, 101, 0, 204, 55]

def fun1(nums):
    
    pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pointer],nums[i] = nums[i],nums[pointer]
            pointer+=1
    return nums

result = fun1(nums)
print(result)
# Problem 2: The Minimal Construction Crew (Variable Window)
# Scenario: You have a list of positive integers representing the cost of materials for each day of a project.
# You need to spend at least target amount of money.
# Requirement: Find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0.
# Input: costs = [2, 3, 1, 2, 4, 3], target = 7
# Expected Output: 2 (The subarray [4, 3] has a sum of 7, and length 2. [2, 3, 1, 2] also sums to >=7 but its length is 4).
# Hint: Expand the window (move right) until sum >= target. Then shrink the window (move left) to see if you can make it 
# smaller while keeping sum >= target.


costs = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_len(nums, target):

    n = len(nums)
    min_len = float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len


print(min_subarray_len(costs, target))
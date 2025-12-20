# Problem 2: The Minimal Construction Crew (Variable Window)
# Scenario: You have a list of positive integers representing the cost of materials for each day of a project.
# You need to spend at least target amount of money.
# Requirement: Find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0.
# Input: costs = [2, 3, 1, 2, 4, 3], target = 7
# Expected Output: 2 (The subarray [4, 3] has a sum of 7, and length 2. [2, 3, 1, 2] also sums to >=7 but its length is 4).
# Hint: Expand the window (move right) until sum >= target. Then shrink the window (move left) to see if you can make it 
# smaller while keeping sum >= target.
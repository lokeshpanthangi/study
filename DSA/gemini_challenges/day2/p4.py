# Problem 4: The Two-Product LimitScenario: An e-commerce warehouse stores items sorted by price in ascending order.
# A customer has a gift card worth exactly target dollars and wants to buy exactly two items that add up to that amount.
# Requirement: Find the 1-based indices of the two items. There is exactly one unique solution. 
# You cannot use the same element twice.Constraint: The input array is already sorted.
# You must use less than $O(N)$ space.
# Input: prices = [2, 7, 11, 15], target = 9 
# Expected Output: [1, 2]



nums = [2, 7, 11, 15]
target = 9

def fun4(nums,target):
    e = len(nums)-1
    s = 0

    while s < e:
        k = nums[s] + nums[e]
        if k == target:
            return [s,e]
        elif k > target:
            e-=1
        else:
            s+=1
    return "None"

result = fun4(nums,target)
print(result)
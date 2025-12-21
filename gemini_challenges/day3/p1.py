# Problem 1: The Network Traffic Spike (Fixed Window)
# Scenario: You are analyzing network traffic. You have an array where each element represents the number of data packets
# received in a specific minute.
# Requirement: Find the maximum total number of packets received in any contiguous k minute interval.
# Input: traffic = [2, 1, 5, 1, 3, 2], k = 3
# Expected Output: 9 (The subarray [5, 1, 3] sums to 9).
# Hint: Calculate the first window sum. Then loop. Remove the left-most element, add the new right-most element.

nums = [1, 5, 10032, 3, 2,99]
k = 3

def fun1(nums,k):
    le = len(nums)
    result = 0
    
    for i in range(k):
        result+=nums[i]
    res = result

    for i in range(k,le):
        result -= nums[i-k]
        result += nums[i]
        res = max(res,result)

    return res


result = fun1(nums,k)
print(result)

# Problem 2: Sorted Data Deduplication

# Scenario: A sensor feeds temperature data into a database. The data is sorted by time, 
# but due to sensor noise, it often records the same temperature multiple times in a row (e.g., 22, 22, 22, 23).

# Requirement: Write a function that modifies the array in-place so that the 
# first k slots contain only the unique temperature readings in their original sorted order. The function should 
# return k (the count of unique elements). It doesn't matter what is left beyond the first k elements.

# Input: [1, 1, 2, 2, 2, 3]

# Expected Output: Return 3. (The array effectively becomes [1, 2, 3, ?, ?, ?])


###### SOLUTION ########

# The question asked is just to find the no of unique elements , without creating extra space the space should be O(1)
# Time wont matter 

def fun2(nums):
    k = len(nums)
    pointer = 0
    for i in range(1,k):
        if nums[i] != nums[pointer]:
            pointer += 1
            nums[pointer] = nums[i]
    return pointer + 1


nums = [1, 1, 2, 2, 2, 3,3,4,6,6,7]
print(fun2(nums))
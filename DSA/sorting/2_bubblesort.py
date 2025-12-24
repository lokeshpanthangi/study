nums = [7,1,2,3,8,7,3,4,1,2,9,1]

def bubble(nums):
    k = len(nums)
    for i in range(k):
        swap = 0
        for j in range(1,k-i):
            if nums[j-1] > nums[j]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
                swap = 1
        if swap == 0:
            break
    return nums

result = bubble(nums)
print(result)
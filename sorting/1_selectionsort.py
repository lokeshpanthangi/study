nums = [7,1,2,3,8,7,3,4,1,2,9,1]

def select(arr):
    k = len(arr)
    for i in range(k):
        curr_min = i
        for j in range(i+1,k):
            if arr[curr_min] > arr[j]:
                curr_min = j
        arr[curr_min],arr[i] = arr[i],arr[curr_min]
    return arr

result = select(nums)
print(result)
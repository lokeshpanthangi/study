nums = [7,1,2,3,8,7,3,4,1,2,9,1]

def insertion(arr):
    k = len(arr)
    for i in range(1,k):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr

result = insertion(nums)
print(result)
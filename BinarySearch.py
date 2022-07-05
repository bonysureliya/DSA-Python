def binary_search(arr,target):
    start = 0
    end = len(arr) -1

    while start <= end:
        mid = start+(end - start )//2

        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1


arr = [1,4,5,6,7,8]
target = 7
ans = binary_search(arr,target)
print(ans)



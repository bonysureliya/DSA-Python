# Array is Sorted so apply binary search
# Find The Greatest number smaller than Target 
# Then inrement it by +1
# then retun it

def SearchInserPosition(arr,target):
	start = 0
	end = len(arr) -1

	while start < end :
		mid = (end - start)//2

		if arr[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
	return start

arr = [1,3,4,6,8,9,19]
target = 3
ans = SearchInserPosition(arr,target)
print(ans)

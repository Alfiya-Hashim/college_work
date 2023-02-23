#implemetation of binary search
def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2


        if arr[mid] == x:
            return mid


        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)


        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1

arr = []
n = int(input("enter number of elements:"))
print("the element of array is:")
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print(arr)

key = int(input("eneter the key value:"))
result = binary_search(arr, 0, len(arr) - 1, key)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
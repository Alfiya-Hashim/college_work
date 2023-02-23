#implementation of insertion sort
arr = []
n = int(input("enter number of elements:"))
print("the element of array is:")
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
insertionSort(arr)
print(arr)




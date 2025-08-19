
def binary_search(nums,  n,  low,  high):
    while low < high:
        mid = int((low + high)/2)

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            low = mid+1
        else:
            high = mid
    return -1


def exponencial_search(arr,  target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] < target:
        i *= 2

    if arr[i] == target:
        return i

    return binary_search(arr,  target,  i//2,  min(i, n-1))


d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
target = 14
result = exponencial_search(d,  target)

print(f"Element found at index {result}")

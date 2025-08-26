
class Solution():
    @staticmethod
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

    def exponencial_search(self, arr,  target):
        if arr[0] == target:
            return 0
        n = len(arr)
        i = 1

        while i < n and arr[i] < target:
            i *= 2

        if arr[i] == target:
            return i

        return Solution.binary_search(arr,  target,  i//2,  min(i, n-1))

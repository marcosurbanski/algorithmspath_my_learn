class Binary:
    def binary_search(nums,  target):
        low = 0
        high = len(nums) - 1
        steps = 0

        while low <= high:
            steps += 1
            mid = (low + high) // 2

            if nums[mid] == target:
                return steps
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

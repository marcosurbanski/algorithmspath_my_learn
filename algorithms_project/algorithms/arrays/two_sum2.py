class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        i = 0

        while i < len(nums) -1:
            if nums[i] + nums[i+1] == target:
                num_dict = [i, i+1]
                print(num_dict)
                return True
            i += 1
        return [-1, -1]
    

solutions = Solution()
a = [2,7,11,15]
target = 150

print(solutions.twoSum(a, target))





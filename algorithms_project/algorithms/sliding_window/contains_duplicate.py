class Numsolution(object):
    def containnumsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        i = 0 

        while i < len(nums):
            j = i + 1
            while j <= i + k and j < len(nums):
                print(f'Comparando nums[{i}] = {nums[i]} com nums[{j}] = {nums[j]}')
                if nums[i] == nums[j]:
                    return True
                j += 1
            i += 1
        return False

numsolution = Numsolution()
print(numsolution.containnumsNearbyDuplicate([1,2,3,1], 3))
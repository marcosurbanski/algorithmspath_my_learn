class Numsolution(object):
    def containnumsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        l, r = 0, 0
        _max = 1
        counter = {}
        index_validator = None

        print(nums)
        print(len(nums))

        counter[nums[0]] = 1

        while r < len(nums) -1:  
            r += 1          
            print(nums[r])
            for r in nums:
                print(r)
                for l in nums:
                    print(l)
                    l += 1
                    if nums[r] == nums[l] and abs(nums[r] - nums[l]) <= k :
                        print(f'Os valores de R: {nums[r]} e L: {nums[l]}')
                        index_validator = True
                        return index_validator 
                    
                     
        return False


numsolution = Numsolution()
print(numsolution.containnumsNearbyDuplicate([1,2,3,1], 3))
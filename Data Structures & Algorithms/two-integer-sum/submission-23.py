class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # t=n[i]+n[j] where i!=j

        #t-n[j]=n[i]

        hashmap = {v:k for (k,v) in enumerate(nums)}

        for i,n in enumerate(nums):
            # This is not expensive
            diff = target-n
            # this is
            if diff in nums[i+1:]:
                # and this as well
                j = nums[i+1:].index(diff)+i+1
                return [i,j]

        return None




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # t=n[i]+n[j] where i!=j

        #t-n[j]=n[i]


        for i,n in enumerate(nums):
            diff = target-n
            if diff in nums[i+1:]:
                j = nums[i+1:].index(diff)+i+1
                return [i,j]

        return None




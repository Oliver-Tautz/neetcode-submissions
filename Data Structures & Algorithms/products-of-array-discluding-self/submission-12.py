from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = prod(nums)
        ret = []
        for i,x in enumerate(nums):
            if x == 0:
                ret.append(math.prod(nums[:i]+nums[i+1:]))
            else:
                ret.append(int(p/x))

        return ret 
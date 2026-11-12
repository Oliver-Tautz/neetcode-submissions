class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # t=n[i]+n[j] where i!=j

        #t-n[j]=n[i]

        hashmap = {v:k for (k,v) in enumerate(nums)}

        for i,n in enumerate(nums):
            # This is not expensive
            diff = target-n
            # this is
            if diff in hashmap and hashmap.get(diff)!=i:
                # and this as well
                j = hashmap.get(diff)
                return [i,j]

        return None




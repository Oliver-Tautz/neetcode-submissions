from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(lambda: 0)
        for n in nums:
            freqs[n]+=1
        most_common = defaultdict(list)
        for n in freqs:
            most_common[freqs[n]].append(n)
        
        sorted_freqs = sorted(most_common.keys())

        ret=[]
        j=1
        i=0
        while i < k:
            if most_common[sorted_freqs[-j]]:
                next_most_common = most_common[sorted_freqs[-j]].pop()
                ret.append(next_most_common)
                i+=1
            else:
                j+=1
        return ret

            
        

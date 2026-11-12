from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        topk = counter.most_common(k)
        return [x for (x,y) in topk]
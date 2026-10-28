class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cts = {}
        res = []

        for n in nums:
            cts[n] = cts.get(n, 0) + 1

        for i in range(k):
            res.append(max(cts, key=cts.get))
            cts.pop(max(cts, key=cts.get))

        return res

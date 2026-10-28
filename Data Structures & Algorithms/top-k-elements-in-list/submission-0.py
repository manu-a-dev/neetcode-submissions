class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cts    = {}
        miheap = []
        res    = []

        for i in range(len(nums)):
            if nums[i] in cts:
                cts[nums[i]] += 1
            else:
                cts[nums[i]] = 1

        for n in cts.keys():
            heapq.heappush(miheap, (cts[n], n))
            if len(miheap) > k:
                heapq.heappop(miheap)

        for i in range(k):
            res.append(heapq.heappop(miheap)[1])

        return res

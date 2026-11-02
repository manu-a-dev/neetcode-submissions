class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ctr = collections.Counter(nums)
        for c in list(ctr.values()):
            if c % 2 != 0:
                return False
        return True
        
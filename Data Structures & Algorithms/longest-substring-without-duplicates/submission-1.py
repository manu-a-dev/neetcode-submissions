class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dummy = ""
        high  = 0
        for i in range(len(s)):
            if not s[i] in dummy:
                dummy += s[i]
                high = max(len(dummy), high)
            else:
                dummy = dummy[dummy.index(s[i]) + 1:] + s[i]
        return high
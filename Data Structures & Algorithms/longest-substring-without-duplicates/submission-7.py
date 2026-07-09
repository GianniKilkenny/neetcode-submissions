class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        m = 0
        for r in range(len(s)):
            m = max(m, len(seen))
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        return max(m, len(seen))


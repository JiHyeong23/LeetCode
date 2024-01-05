class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        used = {}
        index = 0
        longest = 0
        for i, char in enumerate(s):
            if char in used and index <= used[char]:
                index = used[char] + 1
            else:
                longest = max(longest, i-index+1)
            used[char] = i

        return longest
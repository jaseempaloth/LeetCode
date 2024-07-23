# Longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

# Time complexity: O(n)
# Space complexity: O(n)

# Test cases
sn = Solution()
s = "abcabcbb"
print(sn.lengthOfLongestSubstring(s)) # 3


class Solution:
    def lengthOfLongestSubstring(self, s):

        max_length = 0

        for i in range(len(s)):

            seen = ""

            for j in range(i, len(s)):

                if s[j] in seen:
                    break
                else:
                    seen = seen + s[j]

            if len(seen) > max_length:
                max_length = len(seen)

        return max_length
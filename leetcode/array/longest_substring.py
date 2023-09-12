class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_s = ""
        max_counter = 0
        for char in s:
            item_index = temp_s.find(char)
            if item_index != -1:
                if len(temp_s) > max_counter:
                    max_counter = len(temp_s)
                temp_s = temp_s[item_index + 1:] + char
            else:
                temp_s += char
        if len(temp_s) > max_counter:
            max_counter = len(temp_s)
        return max_counter

s = input()
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = ''
        start = -1
        max_len = 0
        i = 0
        while i < len(s):
            if start == -1:
                start = i
                curr = s[i]
            else:
                if not self.isRepeat(s[i], curr):
                    curr += s[i]
                else:
                    start = curr.index(s[i]) + 1
                    curr += s[i]
                    curr = curr[start:]
            if len(curr) > max_len:
                max_len = len(curr)
            i += 1
        return max_len
    
    def isRepeat(self, c, s):
        if c in s:
            return True

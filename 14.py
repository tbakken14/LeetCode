class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = strs[0]
        for s in strs[1:]:
            if len(s) < len(output):
                output = output[:len(s)]
            for i in range(len(output)):
                if s[i] != output[i]:
                    output = output[:i]
                    break
        return output
        

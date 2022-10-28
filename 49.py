class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            w = ''.join(sorted(s))
            if w not in d:
                d[w] = []
            d[w].append(s)
        return list(d.values())

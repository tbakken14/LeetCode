class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        max_len = 0
        words = [""]
        for s in arr:
            if self.validate(s):
                for word in words:
                    uniq = True
                    for c in s:
                        if c in word:
                            uniq = False
                    if uniq:
                        new_word = s + word
                        words.append(new_word)
                        if len(new_word) > max_len:
                            max_len = len(new_word)
        return max_len
    
    def validate(self, word):
        d = {}
        for c in word:
            if not c in d:
                d[c] = 0
            d[c] += 1
        return max(d.values()) == 1

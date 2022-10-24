class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = 0
        total = 0
        for c in s:
            val = 0
            if c =='I':
                val = 1
            elif c == 'V':
                val = 5
                if sub == 1:
                    total -= sub
                    val -= sub
            elif c == 'X':
                val = 10
                if sub == 1:
                    total -= sub
                    val -= sub
            elif c == 'L':
                val = 50
                if sub == 10:
                    total -= sub
                    val -= sub
            elif c == 'C':
                val = 100
                if sub == 10:
                    total -= sub
                    val -= sub
            elif c == 'D':
                val = 500
                if sub == 100:
                    total -= sub
                    val -= sub
            elif c == 'M':
                val = 1000
                if sub == 100:
                    total -= sub
                    val -= sub
            sub = val
            total += val
        return total

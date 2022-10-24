class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            rev = int(s[0] + s[1:][::-1])
        else:
            rev = int(s[::-1])
        if rev >= -2**31 and rev <= 2**31:
            return rev
        else:
            return 0

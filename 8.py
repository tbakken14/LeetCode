class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signs = ['+', '-']
        num = ''
        if len(s) > 1:
            if s[0] in signs:
                num += s[0]
                s = s[1:]
        for d in s:
            if d in digits:
                num += d
            else:
                break
        if num == '' or num == '-' or num == '+':
            return 0
        num = int(num)
        print(num)
        if num > -1 + 2**31:
            return -1 + 2**31
        if num < -2**31:
            return -2**31
        return num

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = ''
        
        carry_over = 0
        for i in range(max(len(a), len(b))):
            out = 0
            index_b = len(b)  - 1 - i
            index_a = len(a) - 1 - i
            if carry_over:
                out += 1
                carry_over = 0 
            if index_a >= 0:
                if int(a[index_a]) == 1:
                    out += 1
            if index_b >= 0:
                if int(b[index_b]) == 1:
                    out += 1
            carry_over = out // 2
            output = str(out % 2) + output
            print(i, out, carry_over, output)
        if carry_over:
            output = '1' + output
        return output

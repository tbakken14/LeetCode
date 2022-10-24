class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = []
        for row in range(numRows):
            rows.append("")
        
        is_down = True
        row = 0
        for c in s:
            rows[row] += c
            if is_down:
                if row == numRows - 1:
                    is_down = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    is_down = True
                    row += 1
                else:
                    row -= 1
        out = ""
        for row in rows:
            out += row
        return out

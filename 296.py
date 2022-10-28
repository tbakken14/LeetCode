class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = []
        y = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    x.append(i)
                    y.append(j)
        y = sorted(y)
        mx = x[len(x)/2]
        my = y[len(y)/2]
        c = 0
        for i in range(len(x)):
            c += abs(x[i] - mx)
            c += abs(y[i] - my)
        return c

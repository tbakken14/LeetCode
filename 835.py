class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        m = 0
        #offset -2 to 2 inclusive in example
        for i in range(-len(img1) + 1, len(img1)):
            for j in range(-len(img1) + 1, len(img1)):
                i_overlap = len(img1) - abs(i)
                j_overlap = len(img1) - abs(j)
                count = 0
                if m >= i_overlap * j_overlap:
                    continue
                else:
                    for i2 in range(i_overlap):
                        for j2 in range(j_overlap):
                            if i < 0:
                                if j < 0:
                                    x = img1[i2 + (len(img1) - i_overlap)][j2 + (len(img1) - j_overlap)]
                                    y = img2[i2][j2]
                                else:
                                    x = img1[i2 + (len(img1) - i_overlap)][j2]
                                    y = img2[i2][j2 + (len(img1) - j_overlap)]
                            else:
                                if j < 0:
                                    x = img1[i2][j2 + (len(img1) - j_overlap)]
                                    y = img2[i2 + (len(img1) - i_overlap)][j2]
                                else:
                                    x = img1[i2][j2]
                                    y = img2[i2 + (len(img1) - i_overlap)][j2 + (len(img1) - j_overlap)]
                            count += x*y
                    if count > m:
                        m = count
        return m

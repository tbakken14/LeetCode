class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out = [-1, -1]
        x = len(nums)
        r1 = [0, x]
        r2 = [0, x]
        while x > 0:
            x = x // 2
            start_i = sum(r1) // 2
            end_i = sum(r2) // 2
            
            if out[0] == -1:
                if start_i == len(nums):
                        return [-1, -1]
                if nums[start_i] < target:
                    r1[0] = start_i + 1 #inclusive
                elif nums[start_i] > target:
                    r1[1] = start_i #exclusive
                else:
                    if start_i == 0:
                        out[0] = start_i
                    elif nums[start_i - 1] < target:
                        out[0] = start_i
                    else:
                        r1[1] = start_i
            
            if out[1] == -1:
                if nums[end_i] < target:
                    r2[0] = end_i + 1 #inclusive
                elif nums[end_i] > target:
                    r2[1] = end_i #exclusive
                else:
                    if end_i + 1 == len(nums):
                        out[1] = end_i
                    elif nums[end_i + 1] > target:
                        out[1] = end_i
                    else:
                        r2[0] = end_i + 1
        print(r1, r2)
        return out
            
        

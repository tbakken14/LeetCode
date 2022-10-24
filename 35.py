class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_i = 0
        max_i = len(nums)
        i = len(nums) // 2
        
        while min_i != max_i:
            if nums[i] == target:
                return i
            if target < nums[i]:
                max_i = i
                i = (min_i + max_i) // 2
            elif target > nums[i]:
                min_i = i + 1
                i = (min_i + max_i) // 2
        if i >= len(nums):
            return i
        if nums[i] > target:
            return i
        return i + 1

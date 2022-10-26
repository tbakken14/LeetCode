class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            nums[i] %= k
        n = 0
        while k*n <= sum(nums):
            if n == 0:
                if self.check_zeros(nums):
                    return True
            else:
                if self.check_x(n * k, nums):
                    return True
            n += 1
        return False
    
    def check_x(self, x, nums):
        count = 0
        queue = []
        for n in nums:
            count += n
            queue.append(n)
            while count > x:
                count -= queue.pop(0)
            if count == x:
                if len(queue) > 1:
                    return True
        return False
                
    def check_zeros(self, nums):
        b = False
        for n in nums:
            if n == 0:
                if b:
                    return True
                else:
                    b = True
            else:
                b = False
        return False

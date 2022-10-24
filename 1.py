class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        s = mergeSort(nums, target)
        
    def findIndexes(self, s, target):
        l = len(s)
        il = 0
        ir = l - 1
        summ = s[]
        while
        
                
    def mergeSort(self, nums):
        l = len(nums)
        if l = 1:
            return nums
        else:
            p = l//2
            left = mergeSort(nums[:p])
            right = mergeSort(nums[p:])
            return merge(left, right)
    
    def merge(self, left, right):
        nums = []
        il = 0
        ir = 0
        while il + ir < len(left) + len(right):
            if il == len(il):
                nums.append(right[ir])
                ir += 1
            elif ir == len(ir)
                nums.append(left[il])
                il += 1
            elif left[il] < right[ir]:
                nums.append(left[il])
                il += 1
            elif left[il] > right[ir]:
                nums.append(right[ir])
                ir += 1
        return nums

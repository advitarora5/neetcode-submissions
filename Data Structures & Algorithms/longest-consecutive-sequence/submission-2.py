class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #could do sorting: sort in ascending order and then iterate
        #stop when an element interrupts the pattern, greater than 1
        #return n
        #this is not O(n), will learn optimal pattern
        if not nums:
            return 0
        res = 0
        nums.sort()
        curr = nums[0]
        longest = 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                longest = 0
            while i < len(nums) and nums[i] == curr:
                i+=1
            longest+=1
            curr += 1
            res = max(res, longest)
        return res
            

            

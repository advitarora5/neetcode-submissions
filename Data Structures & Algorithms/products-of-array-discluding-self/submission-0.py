class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1;
        for i in range (len(nums)):
            for k in range (len(nums)):
                if i == k:
                    continue
                prod = prod * nums[k]
            res.append(prod)
            prod = 1
        return res

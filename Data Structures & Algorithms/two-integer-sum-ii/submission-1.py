class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < r:
            diff = target - numbers[l]
            while (r < len(numbers)):
                if (numbers[r] == diff):
                    return [l + 1, r + 1]
                else:
                    r += 1
            l += 1
            r = l + 1
            
            
from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        for num in nums:
            if map[num] > 1:
                return True
            else:
                continue
        return False

            
        
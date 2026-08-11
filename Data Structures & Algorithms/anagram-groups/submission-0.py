class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings=[]
        seen = [False] * len(strs)
        for i in range(len(strs)):
            if seen[i]:
                continue
            current_group = [strs[i]]
            seen[i] = True
            for j in range(i+1, len(strs)):
                if not seen[j] and sorted(strs[i]) == sorted(strs[j]):
                    current_group.append(strs[j])
                    seen[j] = True
            groupings.append(current_group)
        return groupings
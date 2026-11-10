class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for word in strs:
            new=''.join(sorted(word))
            if new not in group:
                group[new]=[]
            group[new].append(word)
        return list(group.values())
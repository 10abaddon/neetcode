class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store={}
        for el in strs:
            new=''.join(sorted(el))
            if new in store:
                store[new].append(el)
            else:
                store[new]=[el]
        return list(store.values())

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        for el in nums:
            if el in store:
                store[el]+=1
            else:
                store[el]=0
        sorted_nums=sorted(store,key=lambda x:store[x], reverse = True)
        return sorted_nums[:k]
        


        
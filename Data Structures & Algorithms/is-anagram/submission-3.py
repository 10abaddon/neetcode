class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.replace(" ","").lower()
        t=t.replace(" ","").lower()
        if len(s)!=len(t):
            return False
        grat={}
        for i in s:
            if i in grat:
                grat[i]+=1
            else:
                grat[i]=1
        for c in t:
            if c in grat:
                grat[c]-=1
            else:
                return False
        for val in grat.values():
            if val !=0:
                return False
        return True
        
        
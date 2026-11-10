class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict={}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for el in t:
            if el not in dict:
                return False
            dict[el]-=1
            if dict[el]<0:
                return False
                
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            exit ()
        s=s.lower()
        t=t.lower()
        if sorted(s)==sorted(t):
            return True
        else:
             return False
        
        
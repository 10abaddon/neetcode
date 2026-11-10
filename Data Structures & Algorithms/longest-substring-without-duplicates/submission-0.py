class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm=0
        for i in range(len(s)):
            a=[]
            cnt=0
            for j in range(i,len(s)):
                if s[j] not in a:
                    a.append(s[j])
                    cnt+=1
                else:
                    break
            if maxm<cnt:
                maxm=cnt
        return maxm

        
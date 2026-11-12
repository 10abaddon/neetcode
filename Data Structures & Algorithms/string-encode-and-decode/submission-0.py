class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result+=str(len(word))+'#'+word
        return result

    def decode(self, s: str) -> List[str]:
        product=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            new=s[j+1:j+length+1]
            i=j+1+length
            product.append(new)
        return product



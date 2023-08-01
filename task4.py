class Solution:
    def findPoisonedDuration(self, l: List[int], d: int) -> int:
        n=len(l)
        if(n==0):
            return 0
        ans=0
        for i in range(n-1):
            ans+=min(d,l[i+1]-l[i])
        return ans+d
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = sorted(nums)
        ans = []
        for i in range(len(s)-2):
            if i>0 and s[i]==s[i-1]:
                continue
            left = i+1
            right = len(s)-1
            while left < right:
                c = s[i]+s[left]+s[right]
                if c ==0:
                    ans.append([s[i],s[left],s[right]])
                    left+=1
                    right-=1
                    while left < right and s[left]==s[left-1]:
                        left+=1
                    while left < right and s[right]==s[right+1]:    
                        right-=1
                elif c<0:
                    left+=1
                else:
                    right-=1     
        return ans          

        
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = sorted(nums)
        l = set()
        for i in range(len(s)-2):
            left = i+1
            right = len(s)-1
            while left < right:
                c = s[i]+s[left]+s[right]
                if c ==0:
                    t = (s[i],s[left],s[right])
                    l.add(t)
                    left+=1
                    right-=1
                elif c<0:
                    left+=1
                else:
                    right-=1     
        return list(l)            

        
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i in range(len(nums)):
            while dq and dq[0]<=i-k: # taaki currect window ke bahar ke indices remove krr rhe hai  
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]: #remove smaller elements from back 
                dq.pop()
            dq.append(i)    
            if i>=k-1: # ye ki 2 length ki window n aaye 
                ans.append(nums[dq[0]])
        
        return ans        

        
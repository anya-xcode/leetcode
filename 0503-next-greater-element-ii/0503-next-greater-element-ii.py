# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = []

#         for i in range(n):
#             greater = -1

#             for j in range(1, n + 1):
#                 if nums[(i + j) % n] > nums[i]:
#                     greater = nums[(i + j) % n]
#                     break

#             ans.append(greater)

#         return ans     

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            greater = float("-inf")
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    greater = nums[j]
                    break
            if greater ==float("-inf"):
                for k in range(0,i):
                    if nums[k]>nums[i]:
                        greater = nums[k]
                        break
            ans.append(greater) 
        for i in range(0,len(ans)):
            if ans[i]==float('-inf'):
                ans[i]=-1               
        return ans                



        
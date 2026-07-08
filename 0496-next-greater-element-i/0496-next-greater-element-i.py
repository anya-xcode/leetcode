class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            x = nums2.index(i)
            greater = -1
            for j in range(x+1,len(nums2)):
                if nums2[j] > i:
                    greater = nums2[j]
                    break
            ans.append(greater)
        return ans                    


        
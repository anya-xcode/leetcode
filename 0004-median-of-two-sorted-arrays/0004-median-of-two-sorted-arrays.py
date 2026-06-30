class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = []
        i =0
        j =0
        while i< len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                m.append(nums1[i])
                i+=1
            else:
                m.append(nums2[j])    
                j+=1
        while i < len(nums1):  
            m.append(nums1[i])   
            i+=1 
        while j < len(nums2): 
            m.append(nums2[j]) 
            j+=1
        n = len(m)

        if n % 2 == 1:
            return m[n // 2]
        else:
            return (m[n // 2] + m[n // 2 - 1]) / 2    

    

        
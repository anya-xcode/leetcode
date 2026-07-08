class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            greater = -1

            for j in range(1, n + 1):
                if nums[(i + j) % n] > nums[i]:
                    greater = nums[(i + j) % n]
                    break

            ans.append(greater)

        return ans     



        
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing_elements = []
        nums[0]=min(nums)
        nums[-1]=max(nums)

        for i in range(min(nums), max(nums)+1):
            if i not in nums:
                missing_elements.append(i)
        return sorted(missing_elements)
             
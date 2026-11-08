class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            while val in nums:
                nums.remove(val)
            return len(nums)
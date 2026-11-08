class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
    
      nums=sorted(set(nums))
      return len(nums)
  
  
  
  
  #at pyhton  new list allocated at variable  list doesnt change so we have to use slice assignment to change the list in place
  
#using two pointer approach
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        insert_idx=1#
        
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[insert_idx]=nums[i]# 이전과 달랴아 뒤에 기록
                insert_idx+=1
            return insert_idx
        
        
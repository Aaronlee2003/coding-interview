from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        left = 0
        right = len(nums) - 1
        
        for a in range(len(nums)-3):
            
            if a > 0 and nums[a] == nums[a-1]:
                print(f"[Skip a] a={a}, 값={nums[a]} (이전 값과 동일)")
                continue
               
            for b in range(a+1,len(nums)-2):
                if b>a+1 and nums[b] == nums[b-1]:
                    print(f"[Skip b] b={b}, 값={nums[b]} (이전 값과 동일)")
                    continue    
                   
                c=b+1
                d=len(nums)-1
                while c<d:
                    current_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if current_sum == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        print(
                            f"-> [FOUND] 인덱스: ({a}, {b}, {c}, {d}) -> 값: {current_sum} (타겟: {target})"
                        )
                      
                        while c<d and nums[c] == nums[c+1]:
                            c+=1
                        while c<d and nums[d] == nums[d-1]:
                            d-=1
                        c+=1
                        d-=1
                       
                        
                    elif current_sum < target:
                        c+=1
                    else:
                        d-=1
        return res  
               
Solution=Solution()
nums1=[-2,-1,-1,1,1,2,2]
target1=0
result1=Solution.fourSum(nums1,target1)
print(result1)

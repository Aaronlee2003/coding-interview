class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return True
            
            # 1. 중복으로 인해 어느 쪽이 정렬되었는지 알 수 없는 경우
            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
            
            # 2. 왼쪽 구간이 정렬된 경우
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            # 3. 오른쪽 구간이 정렬된 경우
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False
# 双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        left, right = 0, 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            
            right += 1
        
        return left+1

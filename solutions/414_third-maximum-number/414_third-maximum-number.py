class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        top3 = []
        for num in nums[3:]:
            if len(top3) < 3:
                top3.append(num)
            else:
                min_top3 = min(top3)
                if num > min_top3:
                    top3.remove(min_top3)
                    top3.append(num)
        
        return min(top3)
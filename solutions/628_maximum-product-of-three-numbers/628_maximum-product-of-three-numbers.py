# 数学
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        min1, min2 = float("inf"), float("inf")

        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max1, max2, max3 = max1, num, max2
            elif num > max3:
                max1, max2, max3 = max1, max2, num
            
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min1, min2 = min1, num
        
        return max(max1 * max2 * max3, max1 * min1 * min2)
# 数学
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = (1 + n) * n // 2
        return _sum - sum(nums)
# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 数组的长度
        n = len(nums) 
        if not n: return 0

        # 初始化状态
        pre = nums[0]
        ans = pre

        # 状态转移
        for i in range(1, n):
            pre = pre + nums[i] if pre>0 else nums[i]
            ans = max(pre, ans)

        return ans
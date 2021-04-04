class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
            if target - nums[i] in d.keys():
                return [d[target-nums[i]], i]
                # 序号小的放前面
            d[nums[i]] = i

# 哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
            if target - nums[i] in d.keys():
                return [d[target-nums[i]], i]
                # ���С�ķ�ǰ��
            d[nums[i]] = i

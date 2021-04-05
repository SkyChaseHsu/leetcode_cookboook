# 哈希表
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = list()

        for i in range(len(nums)):
            if nums[i] in l:
                return True
            l.append(nums[i])

            # 维护一个大小为k的哈希表
            if len(l) > k:
                l.pop(0)

        return False
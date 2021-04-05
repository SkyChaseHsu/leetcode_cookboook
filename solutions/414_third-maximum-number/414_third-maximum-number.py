# 哈希表
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 注意这里的去重处理
        if len(nums) < 3:
            return max(nums)
    
        top3 = []
        for num in nums:
            if len(top3) < 3 and num not in top3:
                top3.append(num)
            else:
                min_top3 = min(top3)
                if num > min_top3 and num not in top3:
                    top3.remove(min_top3)
                    top3.append(num)

        return min(top3) if len(top3) == 3 else max(top3)
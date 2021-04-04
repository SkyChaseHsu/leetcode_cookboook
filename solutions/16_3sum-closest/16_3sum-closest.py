class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)

        # 小于3个元素无法组成，返回[]
        if length < 3:
            return []

        best = 10**7 # 最好的匹配结果
        def update_best(ans):
            nonlocal best
            if abs(ans-target) < abs(best-target):
                best = ans
        
        res = []
        nums.sort()

        for i in range(length):
            # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, length - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]

                update_best(_sum)
                if _sum == best:
                    if res:
                        res.pop()
                    res.append([nums[i], nums[left], nums[right]])
                if _sum == target:
                    # 如果相等，就是最优解了，直接返回
                    if res:
                        res.pop()
                    res.append([nums[i], nums[left], nums[right]])
                    break
                elif _sum < target:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                else:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
        return best
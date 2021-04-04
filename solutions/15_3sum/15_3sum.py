class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)

        if length < 3:
            return []

        res = []
        nums.sort()
        for i in range(length):
            # 如果当前nums[i]已经大于0了，后面的数也没机会凑成0了
            if nums[i] > 0:
                break

            # 去重
            if i and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, length - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 去重
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif _sum < 0:
                    left += 1
                else:
                    right -= 1

        return res

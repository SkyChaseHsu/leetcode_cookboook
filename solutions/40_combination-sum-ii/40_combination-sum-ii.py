# 排列组合
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort() # 对candidates进行排序，防止出现[1,7,1],然后选出[1,7]和[7,1]这种情况
        self.helper(candidates, [], target)
        return self.res


    def helper(self, candidates, solution, target):
        if target == 0:
            # 相加结果==target,返回解法
            self.res.append(solution)
            return
        elif target < 0:
            # 相加结果>target,返回上一层
            return

        visited = set()
        for i in range(len(candidates)):
            if candidates[i] not in visited:
                visited.add(candidates[i])
            else:
                continue

            # 元素不可以重复使用，所以这里用i+1
            new_candidates = candidates[i+1:]
            new_solution = solution + [candidates[i]]
            self.helper(new_candidates, new_solution, target-candidates[i])
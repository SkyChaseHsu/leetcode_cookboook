# 排列组合
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
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

        for i in range(len(candidates)):
            # 这里使用了i,这样比如[2,3,6,7],2往下递归可以取到2,3,6,7
            # 而如果这一层是3，3往下递归只能取到3,6,7就不会存在重复的问题
            new_candidates = candidates[i:]
            new_solution = solution + [candidates[i]]
            self.helper(new_candidates, new_solution, target-candidates[i])
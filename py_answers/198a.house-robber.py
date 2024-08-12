#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev1 = 0  # 1つ前の家から盗む場合の、合計の最大値
        prev2 = 0  # 2つ前の家から盗む場合の、合計の最大値
        for i in range(len(nums)):
            nowbest = max(prev2 + nums[i], prev1)  # 2つ前までの最大値+今の最大値 or 1つ前までの最大値
            prev2 = prev1
            prev1 = nowbest
        return nowbest
# @lc code=end


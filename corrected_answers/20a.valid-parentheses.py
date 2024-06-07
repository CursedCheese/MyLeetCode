#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in d.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or d[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0
# @lc code=end


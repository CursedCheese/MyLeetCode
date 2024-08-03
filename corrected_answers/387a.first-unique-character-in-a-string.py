#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
import collections

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)
        for i, word in enumerate(s):
            if count[word] == 1:
                return i
        return -1
# @lc code=end


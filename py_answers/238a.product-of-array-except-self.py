class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1

        # res[i-1]までの積をres[i]に入れる。
        # res[0]はその1つ前を1として考えて、1を入れる。
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        # 後ろから数えてres[i+1]までの積をres[i]に乗算する
        # これでres[i]にはnums[i]以外のnumsの積が入る
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        fastとslowの2つのポインタを使用
        fastは0じゃない値を前に探しにいき、slowは0があった時点でその場で止まる。
        fastが0じゃない値を見つけ、slowが0を見つけた時、互いの値を交換する。そして、slowは少しずつ
        非0の数を前に置きながら進んでいく。
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            if nums[slow] != 0:
                slow += 1

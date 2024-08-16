class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0  # これまでの最大の利益
        buy = prices[0]  # 買う金額
        for i in range(1,len(prices)):
            if prices[i] - buy > ans:  # i番目で売る利益がこれまでで一番良さそうなら
                ans = prices[i] - buy  # 答えを更新
            elif buy > prices[i]:  # 買った時より安かったら
                buy = prices[i]  # ここで買った方がこの先は得になる
        return ans
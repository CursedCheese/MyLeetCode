class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 最終的にはleftとrightが重なった点と比べて大きい(1つ右)か小さい(1つ左)かになる
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
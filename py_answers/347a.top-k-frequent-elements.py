class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        l = []
        for i in range(k):
            l.append(count[i][0])
        return l
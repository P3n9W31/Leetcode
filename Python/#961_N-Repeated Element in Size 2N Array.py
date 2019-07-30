class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = set()
        for item in A:
            if item in d:
                return item
            d.add(item)
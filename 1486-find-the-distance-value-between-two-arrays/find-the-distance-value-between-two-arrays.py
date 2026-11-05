import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        res = 0
        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            if (idx == 0 or abs(x - arr2[idx - 1]) > d) and (idx == len(arr2) or abs(x - arr2[idx]) > d):
                res += 1
        return res
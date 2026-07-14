class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        total_len = len(merged)
        
        mid = total_len // 2
        
        if total_len % 2 == 1:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0
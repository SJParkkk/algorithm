from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            index = len(nums1) / 2
            answer = nums1[int(index)]
        else:
            index = len(nums1) - 1 / 2
            answer = (nums1[int(index)] + nums1[int(index)-1])/2
        return answer
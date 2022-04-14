from algorithm.leetcode.median import Solution


def test_find_median_sorted_arrays():
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    output = 2.00000
    assert output == sol.findMedianSortedArrays(nums1, nums2)

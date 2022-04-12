from algorithm.leetcode.two_sum import Solution

nums_1, target_1 = [2, 7, 11, 15], 9
nums_2, target_2 = [3, 2, 4], 6
nums_3, target_3 = [3, 3], 6


def test_two_sum_set():
    assert [0, 1] == Solution.two_sum_set(nums_1, target_1)
    assert [1, 2] == Solution.two_sum_set(nums_2, target_2)
    assert [0, 1] == Solution.two_sum_set(nums_3, target_3)


def test_two_sum_deque():
    assert [0, 1] == Solution.two_sum_set(nums_1, target_1)
    assert [1, 2] == Solution.two_sum_set(nums_2, target_2)
    assert [0, 1] == Solution.two_sum_set(nums_3, target_3)


def test_two_sum_dict():
    assert [0, 1] == Solution.two_sum_set(nums_1, target_1)
    assert [1, 2] == Solution.two_sum_set(nums_2, target_2)
    assert [0, 1] == Solution.two_sum_set(nums_3, target_3)
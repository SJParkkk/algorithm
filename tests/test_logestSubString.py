from algorithm.leetcode.logestSubString import Solution
from conftest import input_string, output_string


def test_length_of_longest_substring(input_string, output_string):
    sol = Solution()
    for i, o in zip(input_string, output_string):
        output = len(o)
        print(i)
        assert output == sol.lengthOfLongestSubstring(i)


def test_length_of_longest_substring_dict(input_string, output_string):
    sol = Solution()
    for i, o in zip(input_string, output_string):
        output = len(o)
        print(i)
        assert output == sol.length_of_longest_substring_dict(i)


def test_length_of_longest_substring_index(input_string, output_string):
    sol = Solution()
    for i, o in zip(input_string, output_string):
        output = len(o)
        assert output == sol.length_of_longest_substring_index(i)
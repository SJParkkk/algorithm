from algorithm.leetcode.logestSubString import Solution


def test_length_of_longest_substring():
    sol = Solution()
    s = "abcabcbb"
    output = len("abc")
    assert output == sol.lengthOfLongestSubstring(s)

    s = "bbbbb"
    output = len("b")
    assert output == sol.lengthOfLongestSubstring(s)

    s = "pwwkew"
    output = len("wke")
    assert output == sol.lengthOfLongestSubstring(s)

    s = "au"
    output = len("au")
    assert output == sol.lengthOfLongestSubstring(s)

    s = "aab"
    output = len("au")
    assert output == sol.lengthOfLongestSubstring(s)

from algorithm.leetcode.PalindromicSubstring import Solution


def test_is_palindromic():
    s = 'aba'
    assert True == Solution.is_palindromic(s)

    s = 'bab'
    assert True == Solution.is_palindromic(s)

    s = 'bb'
    assert True == Solution.is_palindromic(s)


def test_longest_palindrome():
    solution = Solution()

    # s = "babad"
    # assert "bab" == solution.longest_palindrome(s)
    #
    # s = "cbbd"
    # output = "bb"
    # assert output == solution.longest_palindrome(s)
    #
    # s = "a"
    # output = "a"
    # assert output == solution.longest_palindrome(s)
    #
    s = "ac"
    output = "a"
    assert output == solution.longest_palindrome(s)
    #
    s = "bb"
    output = "bb"
    assert output == solution.longest_palindrome(s)

    s = "aaaa"
    output = "aaaa"
    assert output == solution.longest_palindrome(s)
    # s = "klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc"
    # 변태 아니냐 진짜로?

    # assert output == solution.longest_palindrome(s)





from algorithm.programmers.string_compression import Compressor, solution


def test_solution():

    s = 's'
    assert 1 == solution(s)

    s = 'xxxxxxxxxxyyy'
    #10x3y
    assert 5 == solution(s)
    #
    s = 'abcabcdede'
    # 2abcdede
    assert 8 == solution(s)


def test_make():
    size = 1
    string = 's'
    c = Compressor(size, string)
    answer = c.process()
    assert 's' == answer

    string = 'xxxxxxxxxxyyy'
    c = Compressor(size, string)
    answer = c.process()

    assert '10x3y' == answer

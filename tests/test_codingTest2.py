from algorithm.programmers.codingTest2 import solution


def test_solution():
    input = ["??b", "abc", "cc?"]
    ouput = 2
    assert ouput == solution(input)
    input = ["abcabcab","????????"]
    ouput = 0
    assert ouput == solution(input)
    # input = ["aa?"]
    ouput = 3
    assert ouput == solution(input)

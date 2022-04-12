from algorithm.programmers.matrixborder import solution


def test_solution():
    assert [8, 10, 25] == solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
    assert [1, 1, 5, 3] == solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
    assert [1] == solution(100, 97, [[1, 1, 100, 97]])


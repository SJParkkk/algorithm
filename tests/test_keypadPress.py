from algorithm.programmers.keypadPress import Coordinate, solution


def test_solution():
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    # assert False
    assert "LRLLLRLLRRL" == solution(numbers, hand)

    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    assert "LRLLRRLLLRR" == solution(numbers, 'left')
    #
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert "LLRLLRLLRL" == solution(numbers, 'right')


def test_coordinate():

    c = Coordinate()
    k = c.get_x('1')
    assert k == 0
    # map = c.map
    # assert map['1']== [0,3]

    # assert x == 0
    # assert isinstance(x, int)

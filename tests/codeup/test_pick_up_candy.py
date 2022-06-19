"""
3
3 1 4
2 5 4
1 4 1
"""
from algorithm.codeup.pick_up_candy import PickUpCandy, Candies

INPUT = '3 3 1 4 2 5 4 1 4 1'


def test_pick_up_candy():
    assert True


def test_run():
    pick_up_candy = PickUpCandy()
    assert 11 == pick_up_candy.run(INPUT)


def test_orders():
    a = [2, 3, 4, 5, 6]
    candies = Candies(a[0], a[1:])
    # candies.orders = a[1:]
    assert candies.orders == [[3, 4], [5, 6]]

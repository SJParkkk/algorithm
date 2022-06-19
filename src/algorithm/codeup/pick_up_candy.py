from dataclasses import dataclass
from sys import stdin
from typing import List
from itertools import permutations


@dataclass
class Candies:
    total_order: int
    orders: List

    @property
    def orders(self) -> List[List[int]]:
        return self._orders

    @staticmethod
    def max_order(order: List) -> int:
        return max(order)

    @orders.setter
    def orders(self, value):
        a = []
        b = []
        for i, v in enumerate(value):
            a.append(v)
            if len(a) == self.total_order:
                b.append(a)
                a = []
        self._orders = b


@dataclass
class PickUpCandy:

    def run(self, input):
        n = list(map(int, input.split()))
        candies = Candies(n[0], n[1:])
        indexs = permutations(range(candies.total_order))
        max_sum = 0
        for index in indexs:
            total = 0
            for i, order in zip(index, candies.orders):
                total += order[i]
            if total > max_sum:
                max_sum = total
        return max_sum

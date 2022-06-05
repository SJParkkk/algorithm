from collections import deque


class Coordinate:

    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']

    def __init__(self):
        self.map = dict()
        self.coordinate()

    def coordinate(self):
        y = 3
        x = 0
        for number in self.NUMBERS:
            self.map.setdefault(number, [x,y])
            x += 1
            if x == 3:
                y -= 1
                x = 0

    def map(self):
        return self.map

    def get_x(self, num):
        a = self.map[num]
        x, _= a
        return x

    def get_y(self, num):
        _, y = self.map[num]
        return y

    def distance(self, target, num):
        target_x, target_y = self.map[target]
        num_x, num_y = self.map[num]
        result = abs(target_x - num_x) + abs(target_y - num_y)
        return result

    def who_is_closer(self, target, left, right):
        left = self.distance(target, left)
        right = self.distance(target, right)
        result = None
        if left < right:
            result = 'left'
        elif left > right:
            result = 'right'
        return result


def solution(numbers, hand):
    answer = ''
    c = Coordinate()
    current_left = deque(['*'], 1)
    current_right = deque(['#'], 1)
    for number in numbers:
        if c.get_x(number) == 0:
            answer += 'L'
            current_left.append(number)
        elif c.get_x(number) == 2:
            answer += 'R'
            current_right.append(number)
        else:
            default = 'L' if hand == 'left' else 'R'

            if c.who_is_closer(number, current_left[-1], current_right[-1]) == 'left':
                current_left.append(number)
                answer += 'L'
            elif c.who_is_closer(number, current_left[-1], current_right[-1]) == 'right':
                current_right.append(number)
                answer += 'R'
            else:
                current_left.append(number) if default == 'L' else current_right.append(number)
                answer += default
    return answer
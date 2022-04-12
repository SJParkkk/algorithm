from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'val:{self.val} next:{self.next}'

    def __eq__(self, other):
        return (self.val == other.val) and (self.next == other.next)


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        def _get_num(l: ListNode):
            list_num = deque([l.val])
            next = l.next
            while l and next:
                list_num.appendleft(next.val)
                next = next.next
            return list_num
        l1, l2 = _get_num(l1), _get_num(l2)
        sum = str(int(''.join(list(map(str, l1)))) + int(''.join(list(map(str, l2)))))
        prev = None
        for s in sum:
            node = ListNode(val=s, next=prev)
            prev = node
        return node
        # answer = [int(sum[i]) for i in range(len(sum)-1, -1,  -1)]
        # return answer
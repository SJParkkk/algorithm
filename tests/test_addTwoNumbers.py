"""
ex1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
ex2
Input: l1 = [0], l2 = [0]
Output: [0]
ex3
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from algorithm.leetcode.addTwoNumbers import Solution, ListNode


def insert_node(l: list):
    element: ListNode = None
    for i in range(len(l)-1, -1, -1):
        v = l[i]
        if not element:
            element = ListNode(val=v, next=None)
        else:
            element = ListNode(val=v, next=element)
    return element


def test_add_two_numbers():
    # ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
    l1, l2 = [2, 4, 3], [5, 6, 4]
    l1, l2 = insert_node(l1), insert_node(l2)
    # output:ListNode = insert_node([7, 0, 8])
    assert [7, 0, 8] == Solution.addTwoNumbers(l1, l2)
    #
    l1, l2 = [0], [0]
    l1, l2 = insert_node(l1), insert_node(l2)
    assert [0] == Solution.addTwoNumbers(l1, l2)
    #
    l1, l2 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]
    l1, l2 = insert_node(l1), insert_node(l2)
    assert [8, 9, 9, 9, 0, 0, 0, 1] == Solution.addTwoNumbers(l1, l2)

    l1, l2 = [2, 4, 9], [5, 6, 4, 9]
    l1, l2 = insert_node(l1), insert_node(l2)
    assert [7, 0, 4, 0, 1] == Solution.addTwoNumbers(l1, l2)



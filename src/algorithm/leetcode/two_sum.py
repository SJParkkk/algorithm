from collections import deque
from typing import List, Set

class Solution:

    @staticmethod
    def two_sum_set(nums: List[int], target: int) -> List[int]:

        answer: List[Set[int]] = list()
        indexs: Set[int] = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    indexs = {i, j}
                    if indexs not in answer:
                        answer.append(indexs)
                    break
        return list(answer[0])

    @staticmethod
    def two_sum_deque(nums: List[int], target: int) -> List[int]:
        answer = deque(maxlen=2)
        for i in range(len(nums)):
            if len(answer) == 2:
                # 정답을 구한 경우, 이후 연산 진행 X
                break
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.extend([i, j])
                    break
        return list(answer)

    @staticmethod
    def two_sum_dict(nums: List[int], target: int) -> List[int]:
        index_dict = dict()
        for i, v in enumerate(nums):
            if target - v in index_dict:
                return i, index_dict[target - v]
            else:
                index_dict[v] = i

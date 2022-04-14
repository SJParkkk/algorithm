from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        더 긴 배열이 뒤쪽에 있을 경우 슬라이스 인덱스 오류
        :param s:
        :return:
        """
        temp = list()
        indexs = list()
        for i, element in enumerate(s):
            if element in temp:
                indexs.append(i)
                temp = list()
            temp.append(element)
        start = None
        strings = list()
        for end in range(len(s)):
            if end in indexs:
                strings.append(s[start:end])
                start = end
        strings.append(s[start:]) if indexs else strings
        longest: int = max(list(map(len, strings))) if len(strings) > 0 else len(s)
        return longest

    def length_of_longest_substring_dict(self, s: str)->int:
        q = deque()
        items = {}
        max_len = 0

        for c in s:
            if c in items:
                popped_item = None
                while popped_item != c:
                    popped_item = q.popleft()
                    if popped_item in items:
                        items.pop(popped_item)
            q.append(c)
            items[c] = c
            # 최대 길이 저장.
            max_len = max(max_len, len(q))
        return max_len

    def length_of_longest_substring_index(self, s: str)-> int:
        """
        deque 로 구현 방법보다 빠름
        :param s:
        :return:
        """
        words = {}
        start = 0
        answer = 0
        n = len(s)
        for j in range(n):
            char = s[j]
            if char in words and words[char] > start:
                # 반복된 문자 이전 인덱스 저장.
                start = words[char]
            answer = max(answer, j - start + 1)
            words[char] = j + 1
        return answer

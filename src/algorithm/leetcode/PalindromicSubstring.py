from collections import deque


class Solution:

    @staticmethod
    def is_palindromic(s: str):
        count = int(len(s) / 2)
        for i in range(count):
            # 0, -1// 1, -2
            index = -1
            if s[i] != s[index - i]:
                return False
        return True

    def longest_palindrome(self, s: str) -> str:
        answer = ''
        palindromes = deque()
        numbers = [i for i in range(len(s) + 1)]
        numbers_count = len(numbers) if len(numbers) % 2 == 0 else len(numbers) -1
        middle_index = int(numbers_count / 2)
        left, right = numbers[:middle_index], numbers[middle_index:]
        for count in right:
            for i in range(0, len(s)):
                new_s = s[i: i+count]
                if self.is_palindromic(new_s) and len(new_s) == count:
                    palindromes.append(new_s)
        if palindromes:
            answer = palindromes.pop()
            return answer
                # palindromes = deque()
        for count in reversed(right):
            for i in range(0, len(s)):
                new_s = s[i: i + count]
                if self.is_palindromic(new_s) and len(new_s) == count:
                    palindromes.append(new_s)
        if palindromes:
            return palindromes.pop()

        # 중간값 구하고 젤 큰 값 pop 없으면

        # for count in range(len(s) + 1, 0, -1):
        #     for i in range(0, len(s)):
        #         new_s = s[i: i+count]
        #         if self.is_palindromic(new_s) and len(new_s) == count:
        #             palindromes.append(new_s)
        #     if palindromes:
        #         return palindromes.popleft()
        # if not longest_count:
        #     longest_count = len(new_s)
        # if len(new_s) > longest_count:
        #     longest_count = len(new_s)
        # longest_count = max([len(e) for e in answers])
        # for palindrome in palindromes:
        #     if len(palindrome) == longest_count:
        #         answer = palindrome
        #         break

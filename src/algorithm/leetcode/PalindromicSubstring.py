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
        numbers = [i for i in range(len(s) + 1)]
        numbers_count = len(numbers) if len(numbers) % 2 == 0 else len(numbers) -1
        middle_index = int(numbers_count / 2)
        left = middle_index
        right = middle_index-1
        for idx in range(middle_index):
            for i in range(len(s) + 1, 0, -1):
                new_s = s[-(i-right):]
                if self.is_palindromic(new_s):
                    return new_s
                new_s = s[i-left: i]
                if self.is_palindromic(new_s) and len(new_s) == left:
                    return new_s
            left -= 1
            right += 1
        return answer

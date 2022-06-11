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
        answer = '' if len(s) != 1 else s

        for count in range(1, len(s) + 1):
            if len(s) > 2 and count == 1:
                continue
            for i in range(0, len(s)):
                new_s = s[i: i+count]
                if self.is_palindromic(new_s) and len(new_s) == count:
                    return new_s
        return answer

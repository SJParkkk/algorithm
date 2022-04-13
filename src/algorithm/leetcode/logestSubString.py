class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
        longest:int = max(list(map(len, strings))) if len(strings) > 0 else len(s)
        return longest
from collections import deque
from dataclasses import dataclass, field
from typing import Dict


class StringStack:
    def __init__(self):
        self.deq = deque([])

    def push(self, letter):
        self.deq.append(letter)

    def pop(self):
        return self.deq.pop()

    def popleft(self):
        return self.deq.popleft()

    def len(self):
        return self.deq.__len__()

    def last_letter(self):
        if self.len() > 0:
            return self.deq[-1]


@dataclass
class Compressor:

    size: int
    string: str
    letter_count: Dict = field(default_factory=dict)

    def iter_letter(self) -> str:
        element = ''
        if not self.size:
            return None
        for s in self.string:
            element += s
            if len(element) == self.size:
                yield element
                element = ''
        r = self._remainder()
        if r:
            yield self.string[-r:]

    def _remainder(self):
        _, r = divmod(len(self.string), self.size)
        return r

    def process(self):
        deq = StringStack()
        result = ''
        for letter in self.iter_letter():
            last_letter = deq.last_letter()
            if last_letter == letter:
                self.letter_count.setdefault(letter, 1)
                # {'ab' : 2} # abab//cdcd//ab//cd
                self.letter_count[letter] += 1
            else:
                for word, count in self.letter_count.items():
                    deq.pop()
                    result += str(count) + word
                self.letter_count = dict()
                deq.push(letter)

        for word, count in self.letter_count.items():
            deq.pop()
            result += str(count) + word
        for i in range(deq.len()):
            result += deq.popleft()
        if result == '':
            result = self.string
        return result


def solution(s):
    count = int(len(s) / 2)
    word_count = []

    for i in range(0, count+1):
        c = Compressor(i, s)
        r = c.process()
        word_count.append(len(r))
    answer = min(word_count)
    return answer
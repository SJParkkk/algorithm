from dataclasses import dataclass, field
from typing import List, Dict


def solution(id_list, report, k):
    # 누굴 신고 했나
    report_who = {id: set() for id in id_list}

    # 누가 몇번 신고 당했나
    reported_count = {id: set() for id in id_list}

    for r in report:
        report, reported = r.split()
        report_who[report].add(reported)
        reported_count[reported].add(report)

    # 신고 당한 사람
    reported_person = [key for key, v in reported_count.items() if len(v) >= k]
    return [len(list(filter(lambda x: x in reported_person, value))) for key, value in report_who.items()]


@dataclass
class MailParser:
    mails: Dict[str, str]

    def mails(self, report: List[str]) -> Dict[str, str]:
        report = set(report)
        for r in report:
            report, reported =r.split()
        self.mails = {r.split()[0]:r.split()[1] for r in report}
        return self.ma


@dataclass
class Person:
    name: str
    power: int


@dataclass
class User:
    name: str
    power: int
    enemies: List[Person] = field(default_factory=list)

    def add_enemy(self, other: Person):
        self.enemies.append(other)

    def attack(self, other: Person):
        other.power -= 1
        self.add_enemy(other)

    def enemies_not_died(self) -> List[Person]:
        new = [enemy for enemy in self.enemies if enemy.power > 1]
        return new


def solution1(user_names, mail, k):
    users = {name: User(name, k) for name in user_names}
    # 중복 제거

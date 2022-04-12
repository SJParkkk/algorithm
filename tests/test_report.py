from dataclasses import dataclass
from typing import List

import pytest

from algorithm.programmers.report import solution, solution1, User, Person


def test_report():
    assert False


@dataclass
class Info:
    id_list: List[str]
    report: List[str]
    k: int


def first_input() -> Info:
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    return Info(id_list, report, k)


def second_input() -> Info:
    id_list = ["con", "ryan"]
    report: List[str] = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    return Info(id_list, report, k)


def sj() -> User:
    name1 = 'sj'
    power = 2
    sj = User(name1, power)
    return sj


def kr() -> Person:
    name = 'kr'
    power = 2
    kr = Person(name, power)
    return kr

def test_solution():
    assert [2, 1, 1, 0] == solution(first_input().id_list, first_input().report, first_input().k)
    assert [0, 0] == solution(second_input().id_list, second_input().report, second_input().k)


@pytest.mark.skip(reason='not implemented')
def test_solution1():
    assert [2, 1, 1, 0] == solution1(first_input().id_list, first_input().report, first_input().k)
    assert [0, 0] == solution1(second_input().id_list, second_input().report, second_input().k)


def test_attack():
    # name1 = 'sj'
    # power = 2
    # name = 'kr'
    # sj = User(name1, power)
    # kr = Person(name, power)
    sj().attack(kr())
    assert 2 == sj().power
    assert 1 == kr().power


def test_enemies_not_died():
    assert False

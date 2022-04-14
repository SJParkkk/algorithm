import pytest


@pytest.fixture
def input_string():
    inputs = ["dvdf", "abcabcbb", "bbbbb", "pwwkew", "au", "aab"]
    return inputs


@ pytest.fixture
def output_string():
    outputs = ["vdf", "abc", "b", "xke", "au", "ab"]
    return outputs
from util import *


def test_rchop():
    assert rchop('move\t', '\t') == 'move'

from util import rchop


def test_rchop():
    assert rchop('move\t', '\t') == 'move'

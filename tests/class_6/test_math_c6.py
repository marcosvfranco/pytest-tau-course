def test_accumulator_init(accum):
    assert accum.count == 0

def test_accumulator_count_1(accum):
    accum.add()
    assert accum.count == 1

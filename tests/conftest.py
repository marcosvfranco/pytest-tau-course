#Related to Class 6 - Fixtures
import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum():
    yield Accumulator()
    


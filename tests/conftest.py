import sys, os

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add enumerific library path for importing into the tests

import pytest
import enumerific


@pytest.fixture
def EnumSampleA() -> enumerific.Enum:
    """Create and return the sample, EnumSampleA, class for use in the unit tests"""

    class EnumSampleA(enumerific.Enum):
        Value1 = "value1"
        Value2 = "value2"
        Value3 = 3

    return EnumSampleA


@pytest.fixture
def EnumSampleB() -> enumerific.Enum:
    """Create and return the sample, EnumSampleB, class for use in the unit tests"""

    class EnumSampleB(enumerific.Enum):
        Value1 = "value1"
        Value2 = "value2"
        Value3 = 3
        Value4 = 4.5678

    return EnumSampleB

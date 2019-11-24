import pytest
from _pytest.mark import MarkDecorator

unittest: MarkDecorator = pytest.mark.unittest
smoke: MarkDecorator = pytest.mark.smoke
skip: MarkDecorator = pytest.mark.skip

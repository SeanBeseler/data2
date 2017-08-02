"""tests for our pque class"""
from pque import pque
import pytest


@pytest.fixture
def three_pque():
    """Makes a fixture that is a pque with 3 elements."""
    q = pque()
    q.insert('a', 4)
    q.insert('b', 5)
    q.insert('c', 3)
    return q


@pytest.fixture
def empty_pque():
    """Makes a fixture that is a pque with 3 elements."""
    q = pque()
    return q


def test_init(empty_pque):
    """Test the init function"""
    assert len(empty_pque._que) == 0


def test_insert(three_pque):
    """Test the insert function"""
    assert three_pque.pop() == 'b'


def test_insert_error(empty_pque):
    """Test that insert can error"""
    with pytest.raises(ValueError):
        empty_pque.insert('a', 'a')


def test_peek_error(empty_pque):
    """Test that peek can error"""
    with pytest.raises(IndexError):
        empty_pque.peek()


def test_peek_works(three_pque):
    """Test that peek works"""
    assert three_pque.peek() == 'b'


def test_pop_error(empty_pque):
    """Test that pop can error"""
    with pytest.raises(IndexError):
        empty_pque.pop()


def test_pop_works(three_pque):
    """Test that peek works"""
    assert three_pque.pop() == 'b'


def test_pop_works_with_new_head(three_pque):
    """Test that peek works"""
    three_pque.pop()
    assert three_pque.peek() == 'a'

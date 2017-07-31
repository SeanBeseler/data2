"""test for que"""
from dque import dque
import pytest


@pytest.fixture
def empty_dque():
    """ Makes a dque."""
    return(dque())


@pytest.fixture
def three_left_dque():
    """ makes a dque"""
    d = dque()
    d.appendleft(1)
    d.appendleft(2)
    d.appendleft(3)
    return(d)


@pytest.fixture
def three_right_dque():
    """ makes a dque"""
    d = dque()
    d.append(1)
    d.append(2)
    d.append(3)
    return(d)


def test_init_head(empty_dque):
    """Test the init that it has head."""
    assert empty_dque.peek() is None


def test_init_size(empty_dque):
    """Test the init that it has a size."""
    assert empty_dque.size() == 0


def test_append_error(empty_dque):
    """Test that the append can error."""
    with pytest.raises(TypeError):
        empty_dque.append()


def test_append_head(three_right_dque):
    """Test the append works and the head is set."""
    assert three_right_dque.peek() == 3


def test_append_size(three_right_dque):
    """Test the append works and the size is set."""
    assert three_right_dque.size() == 3


def test_append_next_node(three_right_dque):
    """Test the append works and the next node is set."""
    assert three_right_dque._dque.head.next_node.val == 2


def test_append_prev_node(three_right_dque):
    """Test the append works and the prev_node is set."""
    assert three_right_dque._dque.head.next_node.prev_node.val == 1


def test_append_left_error(empty_dque):
    """Test that the append left can error."""
    with pytest.raises(TypeError):
        empty_dque.append()


def test_append_left_head(three_left_dque):
    """Test the append left works and the head is set."""
    assert three_left_dque.peek() == 1


def test_append_left_size(three_left_dque):
    """Test the append left works and the size is set."""
    assert three_left_dque.size() == 3


def test_append_left_next_node(three_left_dque):
    """Test the append left works and the next node is set."""
    assert three_left_dque._dque.head.next_node.val == 2


def test_append_left_prev_node(three_left_dque):
    """Test the append left works and the prev_node is set."""
    assert three_left_dque._dque.head.next_node.prev_node.val == 3


def test_pop_error(empty_dque):
    """Test that pop can error"""
    with pytest.raises(IndexError):
        empty_dque.pop()


def test_pop_left_error(empty_dque):
    """Test that pop left can error"""
    with pytest.raises(IndexError):
        empty_dque.popleft()


def test_pop(three_left_dque):
    """Test that pop works"""
    assert three_left_dque.pop() == 1


def test_pop_left(three_left_dque):
    """Test that pop left works"""
    assert three_left_dque.popleft().val == 3


def test_peek_None(empty_dque):
    """Test that peek returns None"""
    assert empty_dque.peek() is None


def test_peek(three_left_dque):
    """Test that peek works"""
    assert three_left_dque.peek() == 1


def test_peek_left_None(empty_dque):
    """Test that peek left returns None"""
    assert empty_dque.peekleft() is None


def test_peek_left(three_left_dque):
    """Test that peekleft  works"""
    assert three_left_dque.peekleft() == 3


def test_size(three_left_dque):
    """Test that size works"""
    assert three_left_dque.size() == 3


def test_lenght(three_left_dque):
    """Test that len works"""
    assert len(three_left_dque) == 3

"""test for que"""
from que import que
import pytest


@pytest.fixture
def empty_que():
    """ Makes a que."""
    return(que())


@pytest.fixture
def three_que():
    """ makes a que"""
    q = que()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return(q)


def test_init_head(empty_que):
    """Test the init that it has head."""
    assert empty_que.peek() is None


def test_init_size(empty_que):
    """Test the init that it has a size."""
    assert empty_que.size() == 0


def test_enqueue_error(empty_que):
    """Test that the enqueue can error."""
    with pytest.raises(TypeError):
        empty_que.enqueue()


def test_enqueue_head(three_que):
    """Test the enqueue works and the head is set."""
    assert three_que.peek().val == 1


def test_enqueue_size(three_que):
    """Test the enqueue works and the size is set."""
    assert three_que.size() == 3


def test_enqueue_next_node(three_que):
    """Test the enqueue works and the next node is set."""
    assert three_que._que.head.next_node.val == 2


def test_enqueue_prev_node(three_que):
    """Test the enqueue works and the prev_node is set."""
    assert three_que._que.head.next_node.prev_node.val == 1


def test_dequeue(three_que):
    """Test the dequeue works."""
    assert three_que.dequeue() == 1


def test_peek(three_que):
    """Test the peek works."""
    assert three_que.peek().val == 1

def test_len(three_que):
    """Test the dequeue works."""
    assert len(three_que) == 3

"""test for double linked list"""
from double_linked_list import DoubleLinkedList
import pytest


@pytest.fixture
def empty_double_list():
    """ Makes a double linked list."""
    return(DoubleLinkedList())


@pytest.fixture
def three_double_list():
    """ makes a double linked list"""
    d_list = DoubleLinkedList()
    d_list.push(1)
    d_list.push(2)
    d_list.push(3)
    return(d_list)


@pytest.fixture
def three_double_list_append():
    """ makes a double linked list"""
    d_list = DoubleLinkedList()
    d_list.append(1)
    d_list.append(2)
    d_list.append(3)
    return(d_list)


def test_init_tail(empty_double_list):
    """Test the init that it has a tail."""
    assert empty_double_list.tail is None


def test_init_head(empty_double_list):
    """Tes the init that it has head."""
    assert empty_double_list.head is None


def test_init_size(empty_double_list):
    """Test the init that it has a size."""
    assert empty_double_list.size == 0


def test_push_error(empty_double_list):
    """Test that the push and error."""
    with pytest.raises(ValueError):
        empty_double_list.push()


def test_push_head(three_double_list):
    """Test the push works and the head is set."""
    assert three_double_list.head.val == 3


def test_push_tail(three_double_list):
    """Test the push works and the tail is set."""
    assert three_double_list.tail.val == 1


def test_push_size(three_double_list):
    """Test the push works and the size is set."""
    assert three_double_list.size == 3


def test_push_next_node(three_double_list):
    """Test the push works and the next node is set."""
    assert three_double_list.head.next_node.val == 2


def test_push_prev_node(three_double_list):
    """Test the push works and the prev_node is set."""
    assert three_double_list.tail.prev_node.val == 2


def test_append_error(empty_double_list):
    """Test that the append and error."""
    with pytest.raises(ValueError):
        empty_double_list.append()


def test_append_head(three_double_list_append):
    """Test the append works and the head is set."""
    assert three_double_list_append.head.val == 1


def test_append_tail(three_double_list_append):
    """Test the append works and the tail is set."""
    assert three_double_list_append.tail.val == 3


def test_append_size(three_double_list_append):
    """Test the append works and the size is set."""
    assert three_double_list_append.size == 3


def test_append_next_node(three_double_list_append):
    """Test the append works and the next node is set."""
    assert three_double_list_append.head.next_node.val == 2


def test_append_prev_node(three_double_list_append):
    """Test the append works and the prev_node is set."""
    assert three_double_list_append.tail.prev_node.val == 2


def test_pop_error(empty_double_list):
    """Test that the pop and error."""
    with pytest.raises(IndexError):
        empty_double_list.pop()


def test_pop_head(three_double_list_append):
    """Test the pop works and the head is set."""
    assert three_double_list_append.pop().val == 1


def test_pop_tail(three_double_list_append):
    """Test the pop works and the tail is set."""
    three_double_list_append.pop()
    assert three_double_list_append.tail.val == 3


def test_pop_size(three_double_list_append):
    """Test the pop works and the size is set."""
    three_double_list_append.pop()
    assert three_double_list_append.size == 2


def test_pop_next_node(three_double_list_append):
    """Test the pop works and the next node is set."""
    three_double_list_append.pop()
    assert three_double_list_append.head.next_node.val == 3


def test_pop_prev_node(three_double_list_append):
    """Test the pop works and the prev_node is set."""
    three_double_list_append.pop()
    assert three_double_list_append.tail.prev_node.val == 2


def test_pop_all_list_tail(three_double_list_append):
    """Test the pop works and the tail is set."""
    three_double_list_append.pop()
    three_double_list_append.pop()
    three_double_list_append.pop()
    assert three_double_list_append.tail is None


def test_pop_all_list_head(three_double_list_append):
        """Test the pop works and the head is set."""
        three_double_list_append.pop()
        three_double_list_append.pop()
        three_double_list_append.pop()
        assert three_double_list_append.head is None


def test_shift_error(empty_double_list):
    """Test that the shift and error."""
    with pytest.raises(IndexError):
        empty_double_list.shift()


def test_shift_head(three_double_list_append):
    """Test the shfit works and the head is set."""
    assert three_double_list_append.shift() == 3


def test_shift_tail(three_double_list_append):
    """Test the shift works and the tail is set."""
    three_double_list_append.shift()
    assert three_double_list_append.tail.val == 2


def test_shift_size(three_double_list_append):
    """Test the shift works and the size is set."""
    three_double_list_append.shift()
    assert three_double_list_append.size == 2


def test_shift_next_node(three_double_list_append):
    """Test the shift works and the next node is set."""
    three_double_list_append.shift()
    assert three_double_list_append.head.next_node.val == 2


def test_shift_prev_node(three_double_list_append):
    """Test the shift works and the prev_node is set."""
    three_double_list_append.shift()
    assert three_double_list_append.tail.prev_node.val == 1


def test_shift_all_list(three_double_list_append):
    """Test the shift works and the tail and the head is set."""
    three_double_list_append.shift()
    three_double_list_append.shift()
    three_double_list_append.shift()
    assert three_double_list_append.head is None
    assert three_double_list_append.tail is None


def test_remove_error(three_double_list_append):
    """Test that the remove and error."""
    with pytest.raises(ValueError):
        three_double_list_append.remove(10)


def test_remove_head(three_double_list_append):
    """Test the remove works and the head is set."""
    three_double_list_append.remove(1)
    assert three_double_list_append.head.val == 2


def test_remove_tail(three_double_list_append):
    """Test the remove works and the tail is set."""
    three_double_list_append.remove(3)
    assert three_double_list_append.tail.val == 2


def test_remove_size(three_double_list_append):
    """Test the remove works and the size is set."""
    three_double_list_append.remove(2)
    assert three_double_list_append.size == 2


def test_remove_next_node(three_double_list_append):
    """Test the remove works and the next node is set."""
    three_double_list_append.remove(3)
    assert three_double_list_append.head.next_node.val == 2


def test_remove_prev_node(three_double_list_append):
    """Test the remove works and the prev_node is set."""
    three_double_list_append.remove(1)
    assert three_double_list_append.tail.prev_node.val == 2


def test_remove_all_list(three_double_list_append):
    """Test the shift works and the tail and the head is set."""
    three_double_list_append.remove(1)
    three_double_list_append.remove(2)
    three_double_list_append.remove(3)
    assert three_double_list_append.head is None
    assert three_double_list_append.tail is None


def test_len_size(three_double_list_append):
    """Test the len works."""
    assert len(three_double_list_append) == 3

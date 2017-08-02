"""test the stack function"""
from stack import Stack
import pytest


@pytest.fixture
def three_stack():
    """Makes a fixture that is a stack with 3 elements."""
    s_stack = Stack([1, 2, 3])
    return s_stack


@pytest.fixture
def other_stack():
    """Makes a fixture that is a stack with 6 elements."""
    s_stack = Stack([1, 2, 3, 'A', 'B', 'C'])
    return s_stack


@pytest.fixture
def empy_stack():
    """Makes a fixture that is a stack with 0 elements."""
    s_stack = Stack()
    return s_stack


def test_init_stack_head(empy_stack):
    """Test the init on an empty stack, checks the head."""
    assert empy_stack.head is None


def test_init_stack_stack_length(empy_stack):
    """Test the init on an empty stack, checks the length."""
    assert len(empy_stack) == 0


def test_push_empty_stack(empy_stack):
    """Test push on empty stack."""
    empy_stack.push(1)
    assert empy_stack.head.val == 1


def test_push_three_element_stack(three_stack):
    """Test push on three element stack."""
    three_stack.push(1)
    assert three_stack.head.val == 1


def test_push_three_six_stack(other_stack):
    """Test push on six stack."""
    other_stack.push(1)
    assert other_stack.head.val == 1


def test_pop_three_element_stack(three_stack):
    """Test pop on three element stack."""
    assert three_stack.pop().val == 3


def test_pop_three_six_stack(other_stack):
    """Test pop on six stack."""
    assert other_stack.pop().val == 'C'


def test_pop_error(empy_stack):
    """Test that pop can error."""
    with pytest.raises(IndexError):
            empy_stack.pop()


def test_len_empty_stack(empy_stack):
    """Test len on empty stack."""
    assert len(empy_stack) == 0


def test_len_three_element_stack(three_stack):
    """Test len on three element stack."""
    assert len(three_stack) == 3


def test_len_six_element_stack(other_stack):
    """Test len on six stack."""
    assert len(other_stack) == 6

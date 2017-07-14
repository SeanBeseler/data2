"""tests for our linked list class"""
from linked_list import LinkedList
import pytest


@pytest.fixture
def three_linked_list():
    """Makes a fixture that is a linkedlist with 3 elements."""
    l_list = LinkedList([1, 2, 3])
    return l_list


@pytest.fixture
def other_linked_list():
    """Makes a fixture that is a linkedlist with 6 elements."""
    l_list = LinkedList([1, 2, 3, 'A', 'B', 'C'])
    return l_list


@pytest.fixture
def empy_linked_list():
    """Makes a fixture that is a linkedlist with 0 elements."""
    l_list = LinkedList()
    return l_list


def test_init_empty_list_head(empy_linked_list):
    """Test the init on an empty list, checks the head."""
    assert empy_linked_list.head is None


def test_init_empty_list_length(empy_linked_list):
    """Test the init on an empty list, checks the length."""
    assert empy_linked_list.length == 0


def test_init_empty_list_itter_works():
    """Test the init on an list, checks the itter."""
    l_list = LinkedList([1, 2, 3])
    assert l_list.head.val == 3


def test_init_empty_list_itter_error():
    """Test the init on an empty list, checks the itter errors."""
    with pytest.raises(TypeError):
        LinkedList(1)


def test_push_empty_list(empy_linked_list):
    """Test push on empty list."""
    empy_linked_list.push(1)
    assert empy_linked_list.head.val == 1


def test_push_three_element_list(three_linked_list):
    """Test push on three element list."""
    three_linked_list.push(1)
    assert three_linked_list.head.val == 1


def test_push_three_six_list(other_linked_list):
    """Test push on six list."""
    other_linked_list.push(1)
    assert other_linked_list.head.val == 1


def test_push_error(empy_linked_list):
    """Test that push can error."""
    with pytest.raises(ValueError):
            empy_linked_list.push()


def test_pop_three_element_list(three_linked_list):
    """Test pop on three element list."""
    assert three_linked_list.pop().val == 3


def test_pop_three_six_list(other_linked_list):
    """Test pop on six list."""
    assert other_linked_list.pop().val == 'C'


def test_pop_error(empy_linked_list):
    """Test that pop can error."""
    with pytest.raises(IndexError):
            empy_linked_list.pop()


def test_size_empty_list(empy_linked_list):
    """Test size on empty list."""
    assert empy_linked_list.size() == 0


def test_size_three_element_list(three_linked_list):
    """Test size on three element list."""
    assert three_linked_list.size() == 3


def test_size_six_element_list(other_linked_list):
    """Test size on six list."""
    assert other_linked_list.size() == 6


def test_len_empty_list(empy_linked_list):
    """Test len on empty list."""
    assert len(empy_linked_list) == 0


def test_len_three_element_list(three_linked_list):
    """Test len on three element list."""
    assert len(three_linked_list) == 3


def test_len_six_element_list(other_linked_list):
    """Test len on six list."""
    assert len(other_linked_list) == 6


def test_search_three_element_list(three_linked_list):
    """Test search on three element list."""
    assert three_linked_list.search(2).val == 2


def test_search_three_six_list(other_linked_list):
    """Test search on six list."""
    assert other_linked_list.search('A').val == 'A'


def test_search_error(empy_linked_list):
    """Test that search can error."""
    with pytest.raises(ValueError):
            empy_linked_list.search()


def test_search_not_found_three_element_list(three_linked_list):
    """Test search on three element list."""
    assert three_linked_list.search(4) is None


def test_search_not_found_three_six_list(other_linked_list):
    """Test search on six list."""
    assert other_linked_list.search('Z') is None


def test_remove_three_element_list(three_linked_list):
    """Test remove on three element list."""
    node = three_linked_list.search(2)
    three_linked_list.remove(node)
    assert three_linked_list.size() == 2


def test_remove_three_six_list(other_linked_list):
    """Test remove on six list."""
    node = other_linked_list.search('A')
    other_linked_list.remove(node)
    assert other_linked_list.size() == 5


def test_remove_error(empy_linked_list):
    """Test that remove can error."""
    with pytest.raises(ValueError):
            empy_linked_list.remove(10)


def test_display_three_element_list(three_linked_list):
    """Test display on three element list."""
    assert three_linked_list.display() == '(3, 2, 1)'


def test_display_three_six_list(other_linked_list):
    """Test display on six list."""
    assert other_linked_list.display() == '(C, B, A, 3, 2, 1)'


def test_repr_three_element_list(three_linked_list):
    """Test repr on three element list."""
    assert repr(three_linked_list) == '(3, 2, 1)'


def test_repr_three_six_list(other_linked_list):
    """Test reper on six list."""
    assert repr(other_linked_list) == '(C, B, A, 3, 2, 1)'

import pytest
from src.linked_list import (
    LinkedList, 
    Node,
)


@pytest.fixture
def ll():
    ll = LinkedList()
    for i in range(0, 5): 
        ll.addAtTail(i)
    return ll


def test_get_item(ll):
    """Retreive item at a certain index"""
    assert ll.get(-3) == -1
    assert ll.get(0) == 0
    assert ll.get(1) == 1
    assert ll.get(2) == 2
    assert ll.get(3) == 3
    assert ll.get(4) == 4
    assert ll.get(5) == -1

def test_get_size(ll):
    """Get size of linkedlist"""
    assert ll.get_size() == 5
    empty = LinkedList()
    assert empty.get_size() == 0

def test_add_at_head(ll):
    ll.addAtHead(5)
    assert ll.head.data == 5 

    empty_ll = LinkedList()
    empty_ll.addAtHead(1)
    assert empty_ll.head.data == 1

def test_add_at_tail(ll):
    ll.addAtTail(8)
    assert ll.get(5) == 8
    
    empty_ll = LinkedList()
    empty_ll.addAtTail(1)
    assert empty_ll.head.data == 1

def add_at_index(ll):
    pass

def delete_at_index(ll):
    pass
"""Singly Linked List"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        current = self.head

        while current:
            if i == index:
                return current.data
            
            i += 1
            current = current.next
                    
        return -1
    
    def get_size(self):
        
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        size = self.get_size()
        # if the index is out of range, do nothing
        if index < 0 or index > size:
            return

        # if the index is 0, insert at head 
        elif index == 0:
            self.addAtHead(val)

        # if the index represents the end of the list, insert at tail
        elif index == size:
            self.addAtTail(val)

        # middle insert
        else:
            new_node = Node(val)
            prev = self.head
            current = prev.next
            i = 0
            while current:
                # if the prev_node + 1 == index
                if i + 1 == index:
                    prev.next = new_node
                    new_node.next = current
                    break
                else:
                    # set prev node to head (i)
                    # set current node to head.next (j = i + 1)
                    prev = current
                    current = current.next
                    i += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        size = self.get_size()
        if index < 0 or index > size:
            return
        
        elif index == 0:
            new_head = self.head.next
            self.head = new_head
        
        else:
        # middle or end delete
            prev = self.head
            current = prev.next
            i = 0
            while current:
                # if the prev_node + 1 == index
                if i + 1 == index:
                    prev.next = current.next
                    current.next = None
                    break
                else:
                    prev = current
                    current = current.next
                    i += 1
          
    
    


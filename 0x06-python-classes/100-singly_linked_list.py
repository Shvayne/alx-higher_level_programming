#!/usr/bin/python3

class Node:
   """Defines the node of a singly linked list"""
    def __init__(self, data, next_node=None):

        """constructor method for Node
        Args:
            data(int): data of the node
            Next_node (Node): pointer to the next node in list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter method to retrive a data in a node"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter method for data in a node

        Args: value (int) - value to set data to
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter method for next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter method for the next node

        Args:
            value: value of next node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
            self.__next_node = value

class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """contructor for linked list"""
        self.head = None

    def sorted_insert(self, value):
        """insert a new node into the correct sorted position
        Args:
            value(int): value  of the new node
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """returns a string representation of a linked list"""
        current = self.head
        output = ""
        while current:
            output += str(current.data) + "\n"
            current = current.next_node
        return output[:-1]
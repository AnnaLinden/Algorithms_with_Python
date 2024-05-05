# Write a class that implements a sorted Doubly linked list. 
# The list is sorted always. When inserting a new element, 
# the new node will be inserted at the right place given its value.

# For example, after inserting values 9, 5, 7, 1, 3, 
# the list will contain (in this order): [1, 3, 5, 7, 9]

# A skeleton of the class is provided. 
# Implement at least the methods that are defined. 
# You can implement new helper methods if you consider it necessary.
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None
    def next(self):
        return self._next
    def previous(self):
        return self._previous
    def link_next(self, node):
        self._next = node
    def link_previous(self, node):
        self._previous = node
    def value(self):
        return self._data


class Sorted_Doubly_Linked_List:
    def __init__(self):
        self._head_node = None

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    def append(self, data):

        # Implement this method
        new_node = Node(data)
        if self._head_node is None:
            self._head_node = new_node
        elif data < self._head_node.value():
            new_node.link_next(self._head_node)
            self._head_node.link_previous(new_node)
            self._head_node = new_node
        else:
            current = self._head_node
            while current.next() is not None and current.next().value() < data:
                current = current.next()
            if current.next() is not None:
                new_node.link_next(current.next())
                current.next().link_previous(new_node)
            current.link_next(new_node)
            new_node.link_previous(current)



# Example usage:
# l = Sorted_Doubly_Linked_List()
# l.append(9)
# l.append(5)
# l.append(7)
# l.append(1)
# l.append(3)
# l.print_list()  # Output: [1, 3, 5, 7, 9]

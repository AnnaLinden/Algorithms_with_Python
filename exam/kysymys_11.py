# Given a class that implements a Singly linked list structure, 
# implement a method that reverts the list.

# For example, if the list contains [1, 2, 3, 4, 5], 
# after calling the method, the list should contain [5, 4, 3, 2, 1]

# Notice that you don't need to create new nodes, 
# just reorganize the existing ones changing their pointers.

# The skeleton of the the class is provided

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def next(self):
        return self._next

    def link(self, node):
        self._next = node

    def value(self):
        return self._data


class Singly_Linked_List:
    def __init__(self):
        self._head_node = None

    def append(self, data):
        current = self._head_node
        previous = None
        while current is not None:
            previous = current
            current = current.next()
        new_node = Node(data)
        if previous is None:
            self._head_node = new_node
        else:
            previous.link(new_node)

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    def reverse(self):
        # Implement this method
        previous = None
        current = self._head_node
        while current is not None:
            next_node = current.next()
            current.link(previous)
            previous = current
            current = next_node
        self._head_node = previous

# Example usage:
# Create a singly linked list
# sll = Singly_Linked_List()
# sll.append(1)
# sll.append(2)
# sll.append(3)
# sll.append(4)
# sll.append(5)

# print("Original list:")
# sll.print_list()

# # Reverse the list
# sll.reverse()

# print("Reversed list:")
# sll.print_list()
# Given the Sorted_Doubly_Linked_List that you implemented in the previous 
# exercise. Implement a function that merges two of them. The function 
# is actually a method in the class, that accepts another object of the 
# same class as parameter and reorganize the links to merge both list over
#  the current object. No new node is created, they are only reorganized. 
# After the merging, both objects point to the same sorted nodes.

# For example, given list [1, 3, 5, 7, 9] and [0, 2, 4, 6, 8,]. After merging 
# them, both objects contain the same list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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

    def merge(self, other):
        # Implement the method
        if not self._head_node:
            self._head_node = other._head_node
            return
        elif not other._head_node:
            other._head_node = self._head_node
            return

        dummy = Node(None)  # Temporary dummy node to ease merging
        tail = dummy

        left = self._head_node
        right = other._head_node

        # Merge the two lists by re-linking nodes
        while left and right:
            if left.value() < right.value():
                tail.link_next(left)
                left.link_previous(tail)
                left = left.next()
            else:
                tail.link_next(right)
                right.link_previous(tail)
                right = right.next()
            tail = tail.next()

        # Attach the remaining part of the list that still has elements
        remaining = left if left else right
        tail.link_next(remaining)
        if remaining:
            remaining.link_previous(tail)

        # Update the head node of both lists
        self._head_node = other._head_node = dummy.next()
        dummy.next().link_previous(None)

#TEST
#  l1 = Sorted_Doubly_Linked_List()
# l1.append(9)
# l1.append(5)
# l1.append(7)
# l1.append(1)
# l1.append(3)
# print("List 1 before merge:")
# l1.print_list()

# # Create second list and append items
# l2 = Sorted_Doubly_Linked_List()
# l2.append(2)
# l2.append(8)
# l2.append(0)
# l2.append(6)
# l2.append(4)
# print("List 2 before merge:")
# l2.print_list()

# # Merge both lists
# l1.merge(l2)
# print("Merged list:")
# l1.print_list()
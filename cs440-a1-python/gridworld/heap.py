"""Part 2: implement a binary min-heap. YOU EDIT THIS FILE.

Store (priority, item) pairs in an array. Compare priorities, not items.
For index i, the children are 2*i + 1 and 2*i + 2, and the parent is
(i - 1) // 2. Each parent's priority must be at most its children's priorities.

Use your own heap; ready-made priority queues are not allowed. The autograder
checks correctness and the number of priority comparisons.
"""
from __future__ import annotations


class BinaryHeap:
    """A min-heap of ``(priority, item)`` pairs.

    TODO (Part 2a). Implement :meth:`push`, :meth:`pop` and :meth:`__len__`,
    keeping the pairs in ``self.data`` with the smallest priority at index 0.

    The autograder reads ``self.data`` directly and checks the invariant after
    every operation on long random sequences. It also counts comparisons and
    expects the amortised count to stay within a small multiple of ``log2 n``,
    so a re-sorted list is correct but will not fit the budget.
    """

    __slots__ = ("data",)

    def __init__(self):
        #: the heap array: a list of ``(priority, item)`` pairs
        self.data: list[tuple] = []

    def __len__(self) -> int:
        """TODO (Part 2a).  How many pairs are in the heap."""
        return(len(self.data))

    def __bool__(self) -> bool:
        return len(self) > 0

    def push(self, priority, item) -> None:
        """Insert one pair.

        TODO (Part 2a). Append, then sift up: while it is smaller than its
        parent, swap the two.
        """
        self.data.append((priority, item))
        index = len(self.data) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[parent_index][0] > self.data[index][0]:
                temp = self.data[parent_index]
                self.data[parent_index] = self.data[index]
                self.data[index] = temp
                index = parent_index
            else:
                break

    def pop(self):
        """Remove and return the ``item`` with the smallest priority.

        TODO (Part 2a). Save ``data[0]``, move the last element into its
        place, shrink the list, then sift that element down past its smaller
        child.

        Raise ``IndexError`` on an empty heap: that is how your search notices
        the open list has run dry and reports the target unreachable.
        """
        if not self.data:
                    raise IndexError("cannot pop an empty heap")
        
        result = self.data[0][1]
        last = self.data.pop()

        if len(self.data) == 0:
             return result

        self.data[0] = last
        current_index = 0    

        while 2 * current_index + 1 < len(self.data):
            current_node = self.data[current_index]
            smallest_child_index = 2 * current_index + 1
            smallest_child = self.data[2 * current_index + 1]
            # Looks to see if there is something to swap
            if len(self.data) > (2 * current_index + 2) and smallest_child[0] > self.data[2 * current_index + 2][0]:
                smallest_child = self.data[2 * current_index + 2]
                smallest_child_index = 2 * current_index + 2
            # Does the swap here
            if smallest_child[0] < current_node[0]:
                temp = self.data[current_index]
                self.data[current_index] = self.data[smallest_child_index]
                self.data[smallest_child_index] = temp
                current_index = smallest_child_index
            else:
                current_index = smallest_child_index
                break

        return result

    # -- optional --------------------------------------------------------
    def peek(self):
        """The smallest priority without removing it.  Provided."""
        if not self.data:
            raise IndexError("peek from an empty heap")
        return self.data[0][0]

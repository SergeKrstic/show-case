class PriorityQueue:
    def __init__(self):
        self._items = []

    def IsEmpty(self):
        return not self._items

    def Insert(self, item):
        if item not in self._items:
            self._items.append(item)
            self._items = sorted(self._items, reverse=True)

    def Peek(self):
        return self._items[-1]

    def Pop(self):
        return self._items.pop()


class PriorityQ:
    """
    Basic heap based priority queue implementation
    """

    def __init__(self, maxSize):
        self._heap = [0] * (maxSize + 1)
        self._size = 0
        self._maxSize = maxSize

    def _swap(self, index1, index2):
        """
        Used to swap two values
        """
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def _reorderUpwards(self, nodeIndex):
        """
        Given a heap and a node in the heap, this function moves upwards
        through the heap swapping elements until the heap is ordered
        """

        # Move up the heap swapping the elements until the heap is ordered
        while nodeIndex > 1 and self._heap[nodeIndex // 2] < self._heap[nodeIndex]:
            self._swap(nodeIndex // 2, nodeIndex)
            nodeIndex = nodeIndex // 2

    def _reorderDownwards(self, nodeIndex, heapSize):
        """
        Given a heap, the heapSize and a node in the heap, this function
        reorders the elements in a top down fashion by moving down the heap
        and swapping the current node with the greater of its two children
        (provided a child is larger than the current node)
        """
        # Move down the heap from node nodeIndex swapping the elements until
        # the heap is reordered
        while 2 * nodeIndex <= heapSize:
            childIndex = 2 * nodeIndex

            # Set child to largest of nodeIndex's two children
            if (childIndex < heapSize) and (self._heap[childIndex] < self._heap[childIndex + 1]):
                childIndex += 1

            # If this nodeIndex is smaller than its child, swap
            if self._heap[nodeIndex] < self._heap[childIndex]:
                self._swap(childIndex, nodeIndex)

                # Move the current node down the tree
                nodeIndex = childIndex

            else:
                break

    def IsEmpty(self):
        return self._size == 0

    def Insert(self, item):
        """
        To insert an item into the queue it gets added to the end of the heap
        and then the heap is reordered
        :param item:
        :return:
        """
        if self._size + 1 > self._maxSize:
            raise Exception("Max size exceeded")

        self._size += 1

        self._heap[self._size] = item

        self._reorderUpwards(self._size)

    def Pop(self):
        """
        To get the max item the first element is exchanged with the lowest
        in the heap and then the heap is reordered from the top down.
        :return:
        """
        self._swap(1, self._size)
        self._reorderDownwards(1, self._size - 1)
        self._size -= 1
        return self._heap[self._size+1]

    def Peek(self):
        return self._heap[1]


class PriorityQLow:
    """
    Basic 2-way heap based priority queue implementation. This time the priority
    is given to the lowest valued key
    """
    def __init__(self, maxSize):
        self._heap = [0] * (maxSize + 1)
        self._size = 0
        self._maxSize = maxSize

    def _swap(self, index1, index2):
        """
        Used to swap two values
        """
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def _reorderUpwards(self, nodeIndex):
        """
        Given a heap and a node in the heap, this function moves upwards
        through the heap swapping elements until the heap is ordered
        """

        # Move up the heap swapping the elements until the heap is ordered
        while nodeIndex > 1 and self._heap[nodeIndex // 2] > self._heap[nodeIndex]:
            self._swap(nodeIndex // 2, nodeIndex)
            nodeIndex = nodeIndex // 2

    def _reorderDownwards(self, nodeIndex, heapSize):
        """
        Given a heap, the heapSize and a node in the heap, this function
        reorders the elements in a top down fashion by moving down the heap
        and swapping the current node with the greater of its two children
        (provided a child is larger than the current node)
        """
        # Move down the heap from node nodeIndex swapping the elements until
        # the heap is reordered
        while 2 * nodeIndex <= heapSize:
            childIndex = 2 * nodeIndex

            # Set child to largest of nodeIndex's two children
            if (childIndex < heapSize) and (self._heap[childIndex] > self._heap[childIndex + 1]):
                childIndex += 1

            # If this nodeIndex is smaller than its child, swap
            if self._heap[nodeIndex] > self._heap[childIndex]:
                self._swap(childIndex, nodeIndex)

                # Move the current node down the tree
                nodeIndex = childIndex

            else:
                break

    def IsEmpty(self):
        return self._size == 0

    def Insert(self, item):
        """
        To insert an item into the queue it gets added to the end of the heap
        and then the heap is reordered
        :param item:
        :return:
        """
        if self._size + 1 > self._maxSize:
            raise Exception("Max size exceeded")

        self._size += 1

        self._heap[self._size] = item

        self._reorderUpwards(self._size)

    def Pop(self):
        """
        To get the max item the first element is exchanged with the lowest
        in the heap and then the heap is reordered from the top down.
        :return:
        """
        self._swap(1, self._size)
        self._reorderDownwards(1, self._size - 1)
        self._size -= 1
        return self._heap[self._size + 1]

    def Peek(self):
        """
        So we can take a peek at the first in line
        """
        return self._heap[1]


class IndexedPriorityQLow:
    """
    Priority queue based on an index into a set of keys. The queue is
    maintained as a 2-way heap.

    The priority in this implementation is the lowest valued key
    """
    def __init__(self, keys, maxSize):
        """
        You must pass the constructor a reference to the std::vector the PQ
        will be indexing into and the maximum size of the queue.
        :param keys:
        :param maxSize:
        """
        self._heap = [0] * (maxSize + 1)
        self._invHeap = [0] * (maxSize + 1)
        self._vecKeys = keys
        self._size = 0
        self._maxSize = maxSize

    def _swap(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]
        self._invHeap[self._heap[index1]] = index1
        self._invHeap[self._heap[index2]] = index2

    def _reorderUpwards(self, nodeIndex):
        """
        Given a heap and a node in the heap, this function moves upwards
        through the heap swapping elements until the heap is ordered
        """

        # Move up the heap swapping the elements until the heap is ordered
        while nodeIndex > 1 and (self._vecKeys[self._heap[nodeIndex // 2]] > self._vecKeys[self._heap[nodeIndex]]):
            self._swap(nodeIndex // 2, nodeIndex)
            nodeIndex = nodeIndex // 2

    def _reorderDownwards(self, nodeIndex, heapSize):
        """
        Given a heap, the heapSize and a node in the heap, this function
        reorders the elements in a top down fashion by moving down the heap
        and swapping the current node with the greater of its two children
        (provided a child is larger than the current node)
        """
        # Move down the heap from node nodeIndex swapping the elements until
        # the heap is reordered
        while 2 * nodeIndex <= heapSize:
            childIndex = 2 * nodeIndex

            # Set child to largest of nodeIndex's two children
            if (childIndex < heapSize) and (self._vecKeys[self._heap[childIndex]] > self._vecKeys[self._heap[childIndex + 1]]):
                childIndex += 1

            # If this nodeIndex is smaller than its child, swap
            if self._vecKeys[self._heap[nodeIndex]] > self._vecKeys[self._heap[childIndex]]:
                self._swap(childIndex, nodeIndex)

                # Move the current node down the tree
                nodeIndex = childIndex

            else:
                break

    def IsEmpty(self):
        return self._size == 0

    def Insert(self, index):
        """
        To insert an item into the queue it gets added to the end of the heap
        and then the heap is reordered from the bottom up.
        :param index:
        :return:
        """
        if self._size + 1 > self._maxSize:
            raise Exception("Max size exceeded")

        self._size += 1

        self._heap[self._size] = index
        self._invHeap[index] = self._size
        self._reorderUpwards(self._size)

    def Pop(self):
        """
        To get the max item the first element is exchanged with the lowest
        in the heap and then the heap is reordered from the top down.
        :return:
        """
        self._swap(1, self._size)
        self._reorderDownwards(1, self._size - 1)
        self._size -= 1
        item = self._heap[self._size + 1]
        return item

    def Peek(self):
        """
        So we can take a peek at the first in line
        """
        return self._heap[1]

    def ChangePriority(self, index):
        """
        If the value of one of the client key's changes then call this with
        the key's index to adjust the queue accordingly
        :param index:
        :return:
        """
        self._reorderUpwards(self._invHeap[index])

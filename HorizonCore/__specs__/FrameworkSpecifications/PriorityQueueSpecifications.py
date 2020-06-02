import numpy
import unittest

from HorizonCore.Framework.PriorityQueue import PriorityQueue, PriorityQ, PriorityQLow, IndexedPriorityQLow


class PriorityQueueSpecifications(unittest.TestCase):

    def test_SpecifyThatPriorityQueueCanBeConstructed(self):
        # act
        priorityQueue = PriorityQueue()

        # assert
        self.assertEqual(len(priorityQueue._items), 0)

    def test_SpecifyThatItCanBeDeterminedIfTheQueueIsEmpty(self):
        # arrange
        priorityQueue = PriorityQueue()

        # assert
        self.assertEqual(priorityQueue.IsEmpty(), True)

    def test_SpecifyThatAnItemCanBeInserted(self):
        # arrange
        priorityQueue = PriorityQueue()

        # act
        priorityQueue.Insert(4)

        # assert
        self.assertEqual(priorityQueue.IsEmpty(), False)
        self.assertEqual(priorityQueue._items[0], 4)

    def test_SpecifyThatMultipleItemsCanBeInsertedAndOrdered(self):
        # arrange
        priorityQueue = PriorityQueue()

        # act
        priorityQueue.Insert(4)
        priorityQueue.Insert(5)
        priorityQueue.Insert(8)
        priorityQueue.Insert(1)
        priorityQueue.Insert(3)

        # assert
        self.assertEqual(priorityQueue.IsEmpty(), False)
        self.assertEqual(len(priorityQueue._items), 5)
        self.assertEqual(priorityQueue._items[0], 8)
        self.assertEqual(priorityQueue._items[1], 5)
        self.assertEqual(priorityQueue._items[2], 4)
        self.assertEqual(priorityQueue._items[3], 3)
        self.assertEqual(priorityQueue._items[4], 1)

    def test_SpecifyThatPriorityDoesNotContainDuplicates(self):
        # arrange
        priorityQueue = PriorityQueue()

        # act
        priorityQueue.Insert(4)
        priorityQueue.Insert(3)
        priorityQueue.Insert(4)
        priorityQueue.Insert(1)
        priorityQueue.Insert(3)

        # assert
        self.assertEqual(priorityQueue.IsEmpty(), False)
        self.assertEqual(len(priorityQueue._items), 3)
        self.assertEqual(priorityQueue._items[0], 4)
        self.assertEqual(priorityQueue._items[1], 3)
        self.assertEqual(priorityQueue._items[2], 1)

    def test_SpecifyThatFirstItemInQueueCanBeSeen(self):
        # arrange
        priorityQueue = PriorityQueue()

        # act
        priorityQueue.Insert(4)
        priorityQueue.Insert(5)
        priorityQueue.Insert(8)
        priorityQueue.Insert(1)
        priorityQueue.Insert(3)

        # assert
        self.assertEqual(priorityQueue.IsEmpty(), False)
        self.assertEqual(len(priorityQueue._items), 5)
        self.assertEqual(priorityQueue.Peek(), 1)

    def test_SpecifyThatFirstItemCanBeRetrievedFromTheQueue(self):
        # arrange
        priorityQueue = PriorityQueue()

        # act
        priorityQueue.Insert(4)
        priorityQueue.Insert(5)
        priorityQueue.Insert(8)
        priorityQueue.Insert(1)
        priorityQueue.Insert(3)

        # assert
        self.assertEqual(priorityQueue.IsEmpty(), False)
        self.assertEqual(len(priorityQueue._items), 5)
        self.assertEqual(priorityQueue.Pop(), 1)
        self.assertEqual(len(priorityQueue._items), 4)


class PriorityQSpecifications(unittest.TestCase):
    def test_SpecifyThatValuesOnTheHeapCanBeSwapped(self):
        pq = PriorityQ(5)
        pq._heap = [5, 4, 3, 2, 1]

        pq._swap(0, 4)

        self.assertEqual([1, 4, 3, 2, 5], pq._heap)

    def test_SpecifyThatAValueOnTheHeapCanBeReorderUpwards(self):
        pq = PriorityQ(5)
        pq._heap = [5, 4, 2, 1, 3]

        pq._reorderUpwards(4)

        self.assertEqual([5, 4, 3, 1, 2], pq._heap)

    def test_SpecifyThatAValueOnTheHeapCanBeReorderDownwards(self):
        pq = PriorityQ(5)
        pq._heap = [5, 4, 3, 1, 2]

        pq._reorderDownwards(1, 5)

        self.assertEqual([5, 4, 3, 1, 2], pq._heap)

    def test_SpecifyPriorityQWorks(self):
        pq = PriorityQ(20)

        self.assertEqual(True, pq.IsEmpty())

        values = [4, 3, 8, 6, 4, 9, 24, 4, 0, 1, 4]
        for value in values:
            pq.Insert(value)

        self.assertEqual(False, pq.IsEmpty())
        self.assertEqual(24, pq.Peek())
        self.assertEqual([0, 24, 6, 9, 4, 4, 4, 8, 3, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0], pq._heap)

        result = []
        for _ in range(len(values)):
            result.append(pq.Pop())

        self.assertEqual([24, 9, 8, 6, 4, 4, 4, 4, 3, 1, 0], result)
        self.assertEqual([0, 0, 1, 3, 4, 4, 4, 4, 6, 8, 9, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0], pq._heap)

        pq = PriorityQ(1)
        pq.Insert(10)
        self.assertRaises(Exception, pq.Insert, 20)

        for _ in range(100):
            # Create a random set of values
            values = [0] * 20
            for i in range(20):
                values[i] = numpy.random.randint(10)
            numpy.random.shuffle(values)

            # Add them to the priorityQ
            pq = PriorityQ(20)
            for value in values:
                pq.Insert(value)

            # Get ordered values from the priorityQ
            result = []
            for _ in range(len(values)):
                result.append(pq.Pop())

            # Assert that them are indeed in order
            for i in range(len(result)-1):
                self.assertGreaterEqual(result[i], result[i+1])

        for _ in range(100):
            # Create a random set of values
            values = [0] * 20
            for i in range(20):
                values[i] = numpy.random.randint(10)
            numpy.random.shuffle(values)

            # Add them to the priorityQ
            pq = PriorityQ(20)
            for value in values:
                pq.Insert(value)

            # Get half of the ordered values from the priorityQ
            result = []
            for _ in range(len(values)//2):
                result.append(pq.Pop())

            # Add some new values to the priorityQ
            numpy.random.shuffle(values)
            for i in range(len(values) // 2):
                pq.Insert(values[i])

            # Get another half of the ordered values from the priorityQ
            result = []
            for _ in range(len(values) // 2):
                result.append(pq.Pop())

            # Assert that them are indeed in order
            for i in range(len(result)-1):
                self.assertGreaterEqual(result[i], result[i+1])

    def test_SpecifyPriorityQLowWorks(self):
        pq = PriorityQLow(20)

        self.assertEqual(True, pq.IsEmpty())

        values = [4, 3, 8, 6, 4, 9, 24, 4, 0, 1, 4]
        for value in values:
            pq.Insert(value)

        self.assertEqual(False, pq.IsEmpty())
        self.assertEqual(0, pq.Peek())
        self.assertEqual([0, 0, 1, 8, 4, 3, 9, 24, 6, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0], pq._heap)

        result = []
        for _ in range(len(values)):
            result.append(pq.Pop())

        self.assertEqual([0, 1, 3, 4, 4, 4, 4, 6, 8, 9, 24], result)
        self.assertEqual([0, 24, 9, 8, 6, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], pq._heap)

        pq = PriorityQLow(1)
        pq.Insert(10)
        self.assertRaises(Exception, pq.Insert, 20)

        for _ in range(100):
            # Create a random set of values
            values = [0] * 20
            for i in range(20):
                values[i] = numpy.random.randint(100)
            numpy.random.shuffle(values)

            # Add them to the priorityQ
            pq = PriorityQLow(20)
            for value in values:
                pq.Insert(value)

            # Get ordered values from the priorityQ
            result = []
            for _ in range(len(values)):
                result.append(pq.Pop())

            # Assert that them are indeed in order
            for i in range(len(result)-1):
                self.assertLessEqual(result[i], result[i+1])

        for _ in range(100):
            # Create a random set of values
            values = [0] * 20
            for i in range(20):
                values[i] = numpy.random.randint(100)
            numpy.random.shuffle(values)

            # Add them to the priorityQ
            pq = PriorityQLow(20)
            for value in values:
                pq.Insert(value)

            # Get half of the ordered values from the priorityQ
            result = []
            for _ in range(len(values)//2):
                result.append(pq.Pop())

            # Add some new values to the priorityQ
            numpy.random.shuffle(values)
            for i in range(len(values) // 2):
                pq.Insert(values[i])

            # Get another half of the ordered values from the priorityQ
            result = []
            for _ in range(len(values) // 2):
                result.append(pq.Pop())

            # Assert that them are indeed in order
            for i in range(len(result)-1):
                self.assertLessEqual(result[i], result[i+1])


class IndexedPriorityQLowSpecifications(unittest.TestCase):
    def test_SpecifyThatPriorityQueueCanBeConstructed(self):
        # arrange
        costs = [0, 0, 0, 0, 0]

        # act
        priorityQueue = IndexedPriorityQLow(costs, len(costs))

        # assert
        self.assertEqual(6, len(priorityQueue._heap), "_heap")
        self.assertEqual(6, len(priorityQueue._invHeap), "_invHeap")
        self.assertEqual(5, len(priorityQueue._vecKeys), "_vecKeys")
        self.assertEqual(0, priorityQueue._size, "_size")
        self.assertEqual(5, priorityQueue._maxSize, "_maxSize")

    def test_SpecifyThatValueCanBeSwapped(self):
        # arrange
        pq = IndexedPriorityQLow([0], 0)
        pq._heap = [0, 1, 2, 3, 4, 5]
        pq._invHeap = [0, 10, 20, 30, 40, 50]
        pq._vecKeys = [0, 1, 2, 3, 4]

        # act
        pq._swap(1, 3)

        # assert
        self.assertEqual([0, 3, 2, 1, 4, 5], pq._heap, "_heap")
        self.assertEqual([0, 3, 20, 1, 40, 50], pq._invHeap, "_invHeap")
        self.assertEqual([0, 1, 2, 3, 4], pq._vecKeys, "_vecKeys")

    def test_SpecifyThatIndexedPriorityQLowWorks(self):
        costs = [0] * 20
        pq = IndexedPriorityQLow(costs, len(costs))

        costsToInsert = [40, 30, 80, 60, 40, 90, 240, 40, 0, 10, 40]
        for i in range(len(costsToInsert)):
            costs[i] = costsToInsert[i]
            pq.Insert(i)

        self.assertEqual(False, pq.IsEmpty())
        self.assertEqual(8, pq.Peek())
        self.assertEqual([0, 8, 9, 2, 0, 1, 5, 6, 3, 7, 4, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0], pq._heap)

        result = []
        while not pq.IsEmpty():
            result.append(costs[pq.Pop()])

        self.assertEqual([0, 10, 30, 40, 40, 40, 40, 60, 80, 90, 240], result)
        self.assertEqual([0, 6, 5, 2, 3, 10, 0, 4, 7, 1, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0], pq._heap)

        pq = IndexedPriorityQLow([0], 1)
        pq.Insert(0)
        self.assertRaises(Exception, pq.Insert, 2)

        for _ in range(100):
            # Create a random set of values
            costsToInsert = [0] * 20
            for i in range(20):
                costsToInsert[i] = numpy.random.randint(100)
            numpy.random.shuffle(costsToInsert)

            # Add them to the priorityQ
            costs = [0] * 20
            pq = IndexedPriorityQLow(costs, len(costs))
            for i in range(len(costsToInsert)):
                costs[i] = costsToInsert[i]
                pq.Insert(i)

            # Get ordered values from the priorityQ
            result = []
            while not pq.IsEmpty():
                result.append(costs[pq.Pop()])

            # Assert that them are indeed in order
            for i in range(len(result) - 1):
                self.assertLessEqual(result[i], result[i + 1])

        for _ in range(5):
            # Create a random set of values
            costsToInsert = [0] * 20
            for i in range(20):
                costsToInsert[i] = numpy.random.randint(100)
            numpy.random.shuffle(costsToInsert)

            # Add them to the priorityQ
            costs = [0] * 20
            pq = IndexedPriorityQLow(costs, len(costs))
            shuffledIndices = list(range(20))
            numpy.random.shuffle(shuffledIndices)

            for index in range(len(costsToInsert)):
                i = shuffledIndices[index]
                costs[i] = costsToInsert[i]
                pq.Insert(i)

            # Add some new values to the priorityQ
            numpy.random.shuffle(shuffledIndices)
            numpy.random.shuffle(costsToInsert)
            for index in range(len(costsToInsert)//2):
                i = shuffledIndices[index]
                if costsToInsert[i] < costs[i]:
                    costs[i] = costsToInsert[i]
                    pq.ChangePriority(i)

            # Get another half of the ordered values from the priorityQ
            result = []
            for _ in range(len(costsToInsert)):
                result.append(costs[pq.Pop()])

            # Assert that them are indeed in order
            for i in range(len(result) - 1):
                self.assertLessEqual(result[i], result[i + 1])

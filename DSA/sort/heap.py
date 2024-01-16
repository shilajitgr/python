"""
Binary tree - A binary tree is a structure with only one node at the root descending into its 
children, and their grandchildren and so on, each node can have at most 2 children.

Full binary tree - A binary tree which has the maximum number of nodes for each level.

Complete binary tree - A full binary tree from level 0 to n-1 and has all the 
leaf nodes at the last level filled from left to right without any gaps.

Heap - It is a complete binary tree which has two types min heap and max heap.

Operations and complexity -
    - Heapify - O(n)
    - insert - O(logn)
    - get height - log(n) - n is the no. of nodes in the heap
    - delete - O(logn)


Min Heap - It is a complete binary tree where each node is smaller than its children. 
Basis the first line, this heap has its minimum value at its root.

Max Heap - It is a complete binary tree where each node is greater than its children.
Basis the first line, this heap has its maximum value at its root.

Priority Heap - Priority heaps are used to fetch elements from the heap based on the 
highest priority.

Heapify (creating max heap) - Pass through any array(representing a complete binary tree) from
right to left and keep comparing with its max child, three scenarios might occur here:
1. No children - Keep the node as it is
2. Children are smaller than the node -  Keep the node as it is
3. Children is larger than the node - Swap the values of the largest child and the node
PS - The leaf nodes of the tree need no adjusting as they don't have any children.
"""

import math


class heap: # for max heap

    def __init__(self, arr, online):
        """
        arr - list of items to be operated on.
        online - items are not available all at once but will be provided one at a time.
        """
        self.arr = arr
        self.online = online
        self.heap = []
        self.sorted = []

    def heapify(self):
        pass

    # def adjust(self, i):

    def insert(self):
        for i in range(len(self.arr)):
            self.heap.append(self.arr[i])
            adjust = True
            parent = i
            while adjust and parent > 0:
                child = parent
                parent = math.floor((child-1)/2)
                if self.heap[child] > self.heap[parent]:
                    temp = self.heap[child]
                    self.heap[child] = self.heap[parent]
                    self.heap[parent] = temp
                else:
                    adjust = False

    def extract(self):
        for i in range(len(self.heap)):
            temp = self.heap[i]
            self.heap[i] = self.heap[-(i+1)]

            self.heap[-(i+1)] = temp

            adjust = True
            parent = i
            children_base = 2*(parent+1) - 1
            heap_len = len(self.heap) - (i+1)
            while adjust and children_base < heap_len:

                max_adr = children_base
                if children_base + 1 < heap_len:

                    max_adr = children_base + 1
                    if self.heap[max_adr] < self.heap[children_base]:
                        max_adr = children_base
                

                if self.heap[max_adr] > self.heap[parent]:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[max_adr]
                    self.heap[max_adr] = temp
                    parent = max_adr
                    children_base = 2*(parent+1) - 1
                else:
                    adjust = False

    def sort(self):

        if not self.online:
            self.heapify()
        else:
            self.insert()

        self.extract()


# heap_obj = heap([1,4,2,4,6,2,4,8,6], True)
heap_obj = heap([1,4,6,2,8], True)
heap_obj.sort()
print(heap_obj.heap)
# print(heap_obj.sorted)
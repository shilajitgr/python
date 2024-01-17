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
        """
        Heapify (creating max heap) - Pass through any array(representing a complete binary tree) from
        right to left and keep comparing with its max child, three scenarios might occur here:
        1. No children - Keep the node as it is
        2. Children are smaller than the node -  Keep the node as it is
        3. Children is larger than the node - Swap the values of the largest child and the node
        PS - The leaf nodes of the tree need no adjusting as they don't have any children.
        """
        self.heap = self.arr.copy()
        heap_len = len(self.heap)
        for idx in range(len(self.heap)-1, -1, -1):
            
            parent = idx
            adjust = True

            self.heap_adjust(adjust, parent, heap_len)
            # while adjust:
            #     children_base = 2*(parent+1) - 1
            #     if children_base >= heap_len:
            #         adjust = False
            #         continue

            #     max_child = children_base
            #     if max_child + 1 < heap_len:
            #         if self.heap[max_child+1] > self.heap[max_child]:
            #             max_child += 1
                
            #     adjust = False
            #     if self.heap[max_child] > self.heap[parent]:
            #         temp = self.heap[parent]
            #         self.heap[parent] = self.heap[max_child]
            #         self.heap[max_child] = temp
            #         adjust = True
            #         parent = max_child
                    


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
        for i in range(len(self.heap)-1, -1, -1):

            parent = 0
            temp = self.heap[parent]
            self.heap[parent] = self.heap[i]
            self.heap[i] = temp
            adjust = True
            heap_len = i

            self.heap_adjust(adjust, parent, heap_len)

    def heap_adjust(self, adjust, parent, heap_len):

        while adjust:
            children_base = 2*(parent+1) - 1
            if children_base >= heap_len:
                adjust = False
                continue

            max_child = children_base
            if max_child + 1 < heap_len:
                if self.heap[max_child+1] > self.heap[max_child]:
                    max_child += 1
            
            adjust = False
            if self.heap[max_child] > self.heap[parent]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[max_child]
                self.heap[max_child] = temp
                parent = max_child
                children_base = 2*(parent+1) - 1
                adjust = True
                

    def sort(self):

        if not self.online:
            self.heapify()
        else:
            self.insert()

        self.extract()


# heap_obj = heap([1,4,2,4,6,2,4,8,6], True)
num_list = [113,43231,122,243,663,1122,33,1242423,123134,111]
heap_obj = heap(num_list, True)
heap_obj.sort()
print(heap_obj.heap, end="\n")

heap_obj = heap(num_list, False)
heap_obj.sort()
print(heap_obj.heap, end="\n")

num_list.sort()
print(num_list)

# print(heap_obj.sorted)
# Lab-5-
class Heaps:

    def init(self):
        self.heap_array = []

        def insert(self, val):
            self.heap_array.append(val)
            last_val = len(self.heap_array)
            while last_val>0:
                if self.heap_array[(last_val-1 // 2)] > self.heap_array[last_val]:
                    self.heap_array[(last_val -1//2)], self.heap_array[last_val] = self.heap_array[last_val], self.heap_array[(last_val-1 //2)]
                else:
                    break

        def extract_min(self):
            if self.is_empty:
                return None

            min_elem = self.heap_array[0]
            i = 0

            while 2*i+1 < len(self.heap_array):
                if self.heap_array[2*i+1] < self.heap_array[2*i+2]:
                    self.heap_array[i] = self.heap_array[2*i+1]
                if self.heap_array[2*i+1] > self.heap_array[2*i+2]:
                    self.heap_array[i] = self.heap_array[2*i+2]
                i = i+1
            return min_elem

        def is_empty(self):
            return len(self.heap_array) == 0

import Heaps


def read_file():
    h_a = open('test_file.txt')
    he = Heaps.heap_array()
    while h_a.hasnextline:
        h_a.split(',')
        for i in range(h_a):
            he.insert = h_a[i]

    heap_sort(he)


def heap_sort(lst):
    r = []
    h = Heaps
    for num in lst:
        h.insert(num)
    while h.is_empty():
        r.append(h.extract_min())
    return r


read_file()

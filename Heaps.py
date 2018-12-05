class Heaps:

    def __init__(self):
        self.heap_array = []

    def insert(self, val):
        self.heap_array.append(val)
        last_val = len(self.heap_array) - 1
        while last_val > 0:
            if self.heap_array[(last_val-1) // 2] > self.heap_array[last_val]:
                self.heap_array[(last_val -1)//2], self.heap_array[last_val] = self.heap_array[last_val], self.heap_array[(last_val-1) //2]
                last_val = (last_val -1)//2
            else:
                break

    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array[0]
        i = 0

        while 2*i+1 < len(self.heap_array):
            if self.heap_array[2*i+1] < self.heap_array[2*i+2]:
                self.heap_array[0] = self.heap_array[2*i+1]
            if self.heap_array[2*i+1] > self.heap_array[2*i+2]:
                self.heap_array[0] = self.heap_array[2*i+2]
            else:
                self.heap_array[i] = self.heap_array[2*i+1]
        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0

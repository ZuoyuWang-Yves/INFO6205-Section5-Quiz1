from typing import List


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self) -> List:
        """Sorts the array using Insertion Sort."""
        for i in range(1, len(self.array)):
            self.insert(i)
        return self.array

    def insert(self, i):
        """Inserts the 'Transition element' into its correct position in the sorted portion of the array."""
        key = self.array[i]
        j = i - 1
        while j >= 0 and self.array[j] > key:
             self.array[j+1] = self.array[j]
             j -= 1

        self.array[j+1] = key

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

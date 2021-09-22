class Heap:
    def __init__(self, a):
        self.a = a.copy()
        self.n = len(a) - 1
        for i in range(self.n, -1, -1):
            self.sift_down(i)

    def sift_up(self, i):
        while i:
            j = (i - 1) // 2
            if self.a[j] > self.a[i]:
                self.a[j], self.a[i] = self.a[i], self.a[j]
                i = j
            else:
                break

    def sift_down(self, i=0):
        while i * 2 + 1 <= self.n:
            j = i * 2 + 1
            if j + 1 <= self.n and self.a[j] > self.a[j + 1]:
                j += 1
            if self.a[i] > self.a[j]:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j
            else:
                break

    def insert(self, x):
        self.a.append(x)
        self.n += 1
        self.sift_up(self.n)

    def pop_min(self):
        self.a[self.n], self.a[0] = self.a[0], self.a[self.n]
        self.n -= 1
        self.sift_down()
        return self.a[self.n + 1]


def heap_sort(a):
    h = Heap(a)
    return [h.pop_min() for _ in range(len(a))]

class Heap:
    def __init__(self, a, mode=False):
        self.mode = mode
        self.a = [(x, i) for i, x in enumerate(a)]
        self.i = [*range(len(a))]
        self.c = len(a)
        self.n = len(a) - 1
        for i in range(self.n, -1, -1):
            self.sift_down(i)

    def swap(self, i, j):
        self.a[j], self.a[i] = self.a[i], self.a[j]
        self.i[self.a[i][1]] = i
        self.i[self.a[j][1]] = j

    def sift_up(self, i):
        while i:
            j = (i - 1) // 2
            if self.mode:
                i, j = j, i
            if self.a[j] > self.a[i]:
                self.swap(i, j)
                if not self.mode:
                    i = j
            else:
                break

    def sift_down(self, i=0):
        while i * 2 + 1 <= self.n:
            j = i * 2 + 1
            if j + 1 <= self.n and (self.a[j] < self.a[j + 1] if self.mode else self.a[j] > self.a[j + 1]):
                j += 1
            if self.mode:
                i, j = j, i
            if self.a[i] > self.a[j]:
                self.swap(i, j)
                if not self.mode:
                    i = j
            else:
                break

    def insert(self, x):
        if len(self.a) == self.n + 1:
            self.a.append((x, self.c))
        else:
            self.a[self.n + 1] = (x, self.c)
        self.i.append(self.n + 1)
        self.c += 1
        self.n += 1
        self.sift_up(self.n)

    def pop(self, i):
        i = self.i[i]
        self.a[i], self.a[self.n] = self.a[self.n], self.a[i]
        self.i[self.a[i][1]] = i
        self.i[self.a[self.n][1]] = -1
        self.n -= 1
        self.sift_down(i)
        self.sift_up(i)
        return self.a[self.n + 1]

    def pop_min(self):
        self.a[self.n], self.a[0] = self.a[0], self.a[self.n]
        self.i[self.a[0][1]] = 0
        self.i[self.a[self.n][1]] = -1
        self.n -= 1
        self.sift_down()
        return self.a[self.n + 1]


def heap_sort(a, reverse=False):
    h = Heap(a, reverse)
    return [h.pop_min() for _ in range(len(a))]



class DoubleHeap():
    def __init__(self, a=[]):
        self.mn = Heap(a)
        self.mx = Heap(a, mode=True)

    def pop_min(self):
        x, i = self.mn.pop_min()
        self.mx.pop(i)
        return x

    def pop_max(self):
        x, i = self.mx.pop_min()
        self.mn.pop(i)
        return x

    def insert(self, x):
        self.mn.insert(x)
        self.mx.insert(x)


a = DoubleHeap()
a.insert(1)
a.insert(2)
a.insert(3)
print(a.pop_max(), a.pop_min())
a.insert(1)
a.insert(0)
a.insert(100)
print(a.pop_max(), a.pop_min())

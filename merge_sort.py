# merge sort with cnt of inversions

def merge(a, b):
    rev = i = j = 0
    c = []
    while i < len(a) or j < len(b):
        if i == len(a) or (j != len(b) and b[j] < a[i]):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            rev += j
            i += 1
    return c, rev


def sort(x):
    if len(x) == 1:
        return x, 0
    lx, rx = x[:len(x)//2], x[len(x)//2:]
    lx, revl = sort(lx)
    rx, revr = sort(rx)
    res, rev = merge(lx, rx)
    return res, rev + revl + revr


input()
print(sort([*map(int, input().split())])[1])

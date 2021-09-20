def sift_up(a, i):
    while i:
        j = (i - 1) // 2
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
            i = j
        else:
            break


def sift_down(a, i=0):
    global n
    while i * 2 + 1 <= n:
        j = i * 2 + 1
        if j + 1 <= n and a[j] > a[j + 1]:
            j += 1
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            i = j
        else:
            break


def pop_min(a):
    global n
    a[n], a[0] = a[0], a[n]
    n -= 1
    sift_down(a)


def heap_sort(a):
    for i in range(n, -1, -1):
        sift_down(a, i)
    for _ in ' ' * len(a):
        pop_min(a)


a = [*map(int, input().split())]
n = len(a) - 1
heap_sort(a)
print(*reversed(a))

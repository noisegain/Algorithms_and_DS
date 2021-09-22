from random import randint


def sort(a, l, r):
    if r - l <= 1:
        return
    x = a[randint(l, r - 1)]
    l0 = l1 = l2 = 0
    for i in range(l, r):
        if a[i] > x:
            l2 += 1
            continue
        j1 = l + l0
        if a[i] < x and l1 >= 1:
            a[i], a[j1] = a[j1], a[i]
            l0 += 1
            l1 -= 1
        j2 = l + l0 + l1
        a[i], a[j2] = a[j2], a[i]
        if a[j1] < x:
            l0 += 1
        else:
            l1 += 1
    sort(a, l, j1)
    sort(a, j2, r)

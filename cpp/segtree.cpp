#include <bits/stdc++.h>

// sum segtree

using ll = long long;
using namespace std;


struct segtree {

    vector<ll> tree;
    int size = 1;

    segtree(int n) {
        while ((size <<= 1) < n);
        tree.resize(size << 1);
        for (int i = size; i < size + n; i++) {
            cin >> tree[i];
        }
        for (int i = size - 1; i > 0; i--) {
            tree[i] = tree[i << 1] + tree[(i << 1) + 1];
        }
    }

    void set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1) {
            tree[x] = v;
            return;
        }
        int m = (lx + rx) >> 1;
        if (i < m) {
            set(i, v, x << 1, lx, m);
        } else {
            set(i, v, (x << 1) + 1, m, rx);
        }
        tree[x] = tree[x << 1] + tree[(x << 1) + 1];
    }

    void set(int i, int v) {
        set(i, v, 1, 0, size);
    }

    ll get(int l, int r, int x, int lx, int rx) {
        if (l >= rx || r <= lx) {
            return 0;
        }
        if (lx >= l && rx <= r) {
            return tree[x];
        }
        int m = (lx + rx) >> 1;
        return get(l, r, x << 1, lx, m) + get(l, r, (x << 1) + 1, m, rx);
    }

    ll get(int l, int r) {
        return get(l, r, 1, 0, size);
    }

};

int main() {
    return 0;
}
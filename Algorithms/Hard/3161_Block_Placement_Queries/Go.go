func getResults(queries [][]int) []bool {
    n := min(50000, len(queries)*3)
    seg := make([]int, n << 2)

    var update func(idx, val, p, l, r int)
    update = func(idx, val, p, l, r int) {
        if l == r {
            seg[p] = val
            return
        }

        mid := (l+r) >> 1
        if idx <= mid {
            update(idx, val, p << 1, l, mid)
        } else {
            update(idx, val, p << 1 | 1, mid+1, r)
        }

        seg[p] = max(seg[p << 1], seg[p << 1 | 1])
    }

    var query func(L, R, p, l, r int) int
    query = func(L, R, p, l, r int) int {
        if L <= l && r <= R {
            return seg[p]
        }

        mid, res := (l+r) >> 1, 0
        if L <= mid {
            res = max(res, query(L, R, p << 1, l, mid))
        }

        if R > mid {
            res = max(res, query(L, R, p << 1 | 1, mid+1, r))
        }

        return res
    }

    tree := redblacktree.NewWithIntComparator()
    tree.Put(0, struct{}{})
    tree.Put(n, struct{}{})
    update(n, n, 1, 0, n)

    result := make([]bool, 0)
    for _, q := range queries {
        if q[0] == 1 {
            x := q[1]
            r := n
            if node, ok := tree.Ceiling(x+1); ok {
                r = node.Key.(int)
            }
            l := 0
            if node, ok := tree.Floor(x-1); ok {
                l = node.Key.(int)
            }

            update(x, x-l, 1, 0, n)
            update(r, r-x, 1, 0, n)
            tree.Put(x, struct{}{})
        } else {
            x, sz := q[1], q[2]
            pre := 0
            if node, ok := tree.Floor(x); ok {
                pre = node.Key.(int)
            }

            result = append(result, max(x-pre, query(0, pre, 1, 0, n)) >= sz)
        }
    }

    return result
}

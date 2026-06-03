func maximumSaleItems(items [][]int, budget int) int {
    n, freq, mx := len(items), make(map[int]int), 0
    for _, item := range items {
        freq[item[0]]++
        mx = max(mx, item[0])
    }

    factor := make(map[int]int)
    for v, _ := range freq {
        for m := v; m <= mx; m += v {
            if _, ok := freq[m]; ok {
                factor[v] += freq[m]
            }
        }
        factor[v]--
    }
    
    type Item struct {
        v, cost, c int
        f float64
    }

    pre, mn := make([]Item, n), math.MaxInt
    for i := 0; i < n; i++ {
        v, cost := items[i][0], items[i][1]
        c, f := factor[v], float64(cost)
        mn = min(mn, cost)
        if c > 0 {
            f /= 2.0
        }

        pre[i] = Item{v, cost, c, f}
    }

    sort.Slice(pre, func(i, j int) bool {
        if pre[i].f == pre[j].f {
            return pre[i].c > pre[j].c
        }
        return pre[i].f < pre[j].f
    })
    
    result, cnt := budget/mn, 0
    for _, item := range pre {
        c := min(item.c, budget/item.cost)
        cnt += c << 1
        budget -= c*item.cost
        result = max(result, cnt + (budget/mn))
    }

    return result
}

func minimumCost(cost []int) int {
    slices.SortFunc(cost, func (i, j int) int {
        return cmp.Compare(j, i)
    })

    result, n := 0, len(cost)
    for i := 0; i < n; i += 3 {
        result += cost[i]
        if i+1 < n {
            result += cost[i+1]
        }
    }

    return result
}

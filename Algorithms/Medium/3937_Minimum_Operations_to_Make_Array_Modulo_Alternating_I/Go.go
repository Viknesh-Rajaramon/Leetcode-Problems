func minOperations(nums []int, k int) int {
    absInt := func (n int) int {
        if n < 0 {
            return -n
        }

        return n
    }
    
    for i := range nums {
        nums[i] %= k
    }
            
    cost_odd := make([]int, k)
    cost_even := make([]int, k)
    for i, num := range nums {
        for target := 0; target < k; target++ {
            d := absInt(num-target)
            c := min(d, k-d)

            if i%2 == 0 {
                cost_even[target] += c
            } else {
                cost_odd[target] += c
            }
        }
    }

    result := math.MaxInt
    for x := 0; x < k; x++ {
        for y := 0; y < k; y++ {
            if x == y {
                continue
            }

            result = min(result, cost_even[x]+cost_odd[y])
        }
    }

    return result
}

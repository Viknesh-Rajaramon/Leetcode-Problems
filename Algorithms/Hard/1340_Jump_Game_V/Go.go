func maxJumps(arr []int, d int) int {
    n := len(arr)
    dp := make([]int, n)
    for i := 0; i < n; i++ {
        dp[i] = 1
    }

    var stack []int
    for i := 0; i <= n; i++ {
        for len(stack) > 0 && (i == n || arr[stack[len(stack)-1]] < arr[i]) {
            var indices []int
            indices = append(indices, stack[len(stack)-1])
            stack = stack[ : len(stack)-1]
            for len(stack) > 0 && arr[stack[len(stack)-1]] == arr[indices[0]] {
                indices = append(indices, stack[len(stack)-1])
                stack = stack[ : len(stack)-1]
            }

            for _, j := range indices {
                if i < n && i-j <= d {
                    dp[i] = max(dp[i], dp[j]+1)
                }

                if len(stack) > 0 && j-stack[len(stack)-1] <= d {
                    dp[stack[len(stack)-1]] = max(dp[stack[len(stack)-1]], dp[j]+1)
                }
            }
        }
        
        if i < n {
            stack = append(stack, i)
        }
    }

    result := dp[0]
    for i := range dp {
        result = max(result, dp[i])
    }
    
    return result
}

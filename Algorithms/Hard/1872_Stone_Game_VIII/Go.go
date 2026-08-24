package main

func stoneGameVIII(stones []int) int {
	n := len(stones)
	for i := 1; i < n; i++ {
		stones[i] += stones[i-1]
	}

	result := stones[n-1]
	for i := n - 2; i > 0; i-- {
		result = max(result, stones[i]-result)
	}

	return result
}

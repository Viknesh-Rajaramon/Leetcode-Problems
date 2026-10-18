package main

func numOfWays(nums []int) int {
	mod, n := int(1e9+7), len(nums)
	comb := make([][]int, n+1)
	for i := range comb {
		comb[i] = make([]int, i+1)
		comb[i][0], comb[i][i] = 1, 1
		for j := 1; j < i; j++ {
			comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % mod
		}
	}

	var dfs func([]int) int
	dfs = func(nums []int) int {
		n := len(nums)
		if n <= 2 {
			return 1
		}

		left, right := make([]int, 0), make([]int, 0)
		for _, num := range nums[1:] {
			if num < nums[0] {
				left = append(left, num)
			} else {
				right = append(right, num)
			}
		}

		return (dfs(left) * dfs(right) % mod) * comb[n-1][len(left)] % mod
	}

	return (dfs(nums) - 1 + mod) % mod
}

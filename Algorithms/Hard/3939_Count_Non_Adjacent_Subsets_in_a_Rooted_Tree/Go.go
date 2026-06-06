package main

func countValidSubsets(parent []int, nums []int, k int) int {
	const mod = 1_000_000_007
	n := len(parent)
	dp0, dp1 := make([][]int64, n), make([][]int64, n)
	for i := 0; i < n; i++ {
		dp0[i], dp1[i] = make([]int64, k), make([]int64, k)
		dp0[i][0], dp1[i][nums[i]%k] = 1, 1
	}

	for i := n - 1; i > 0; i-- {
		p_nz_0, p_nz_1, child_ways_any := make([]int64, 0), make([]int64, 0), make([]int64, k)
		c_nz_any, c_nz_0 := make([]int64, 0), make([]int64, 0)
		for r := 0; r < k; r++ {
			if dp0[parent[i]][r] > 0 {
				p_nz_0 = append(p_nz_0, int64(r))
			}

			if dp1[parent[i]][r] > 0 {
				p_nz_1 = append(p_nz_1, int64(r))
			}

			child_ways_any[r] = (dp0[i][r] + dp1[i][r]) % mod
			if child_ways_any[r] > 0 {
				c_nz_any = append(c_nz_any, int64(r))
			}

			if dp0[i][r] > 0 {
				c_nz_0 = append(c_nz_0, int64(r))
			}
		}

		new_dp0, new_dp1 := make([]int64, k), make([]int64, k)
		for _, r1 := range p_nz_0 {
			for _, r2 := range c_nz_any {
				idx := (r1 + r2) % int64(k)
				new_dp0[idx] = (new_dp0[idx] + dp0[parent[i]][r1]*child_ways_any[r2]) % mod
			}
		}

		for _, r1 := range p_nz_1 {
			for _, r2 := range c_nz_0 {
				idx := (r1 + r2) % int64(k)
				new_dp1[idx] = (new_dp1[idx] + dp1[parent[i]][r1]*dp0[i][r2]) % mod
			}
		}

		dp0[parent[i]], dp1[parent[i]] = new_dp0, new_dp1
	}

	return int((dp0[0][0] + dp1[0][0] - 1) % mod)
}

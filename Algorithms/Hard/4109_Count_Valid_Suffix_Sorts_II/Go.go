package main

func countSuffix(nums []int, target []int) []int {
	n, m := len(nums), len(target)
	result, com := make([]int, m-n+1), append(append(append([]int{}, nums...), 0), target...)
	L_com := len(com)
	z, l, r := make([]int, L_com), 0, 0
	for i := 1; i < L_com; i++ {
		if i <= r {
			z[i] = min(r-i+1, z[i-l])
		}

		for i+z[i] < L_com && com[z[i]] == com[i+z[i]] {
			z[i]++
		}

		if i+z[i]-1 > r {
			l, r = i, i+z[i]-1
		}
	}

	pre := make([]int, m)
	for i := 1; i < m; i++ {
		pre[i] = i
		if target[i-1] >= target[i] {
			pre[i] = pre[i-1]
		}
	}

	freq, bad := make([]int, 100001), 0
	for _, x := range nums {
		if freq[x] == 1 {
			bad--
		}

		freq[x]--
	}

	for i := range n {
		if freq[target[i]] == 0 {
			bad++
		}

		freq[target[i]]++
	}

	zs := n + 1
	for k := range m - n + 1 {
		if bad == 0 {
			min_I := max(0, pre[k+n-1]-k)
			max_I := min(n-1, z[zs+k])
			if max_I >= min_I {
				result[k] = max_I - min_I + 1
			}
		}

		if k+n < m {
			if freq[target[k]] == 1 {
				bad--
			}

			freq[target[k]]--
			if freq[target[k+n]] == 0 {
				bad++
			}

			freq[target[k+n]]++
		}
	}

	return result
}

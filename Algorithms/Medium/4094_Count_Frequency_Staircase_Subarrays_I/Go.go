package main

func countStaircase(nums []int) int {
	n := len(nums)
	ind, pos := make([]int, n), make(map[int][]int)
	for i, a := range nums {
		ind[i] = len(pos[a])
		if _, ok := pos[a]; !ok {
			pos[a] = make([]int, 0)
		}

		pos[a] = append(pos[a], i)
	}

	result := 0
	for i := range n {
		seen, l, r := make(map[int]bool), i, n-1
		for j := i; j < n; j++ {
			if j > r {
				break
			}

			if seen[nums[j]] {
				continue
			}

			seen[nums[j]] = true
			k := len(seen)
			if ind[j]+k-1 >= len(pos[nums[j]]) {
				break
			}

			l = max(l, pos[nums[j]][ind[j]+k-1])
			nxt := n - 1
			if ind[j]+k < len(pos[nums[j]]) {
				nxt = pos[nums[j]][ind[j]+k]
			}

			r = min(r, nxt)
			if l > r {
				break
			}

			tmp := i + k*(k+1)/2 - 1
			if l <= tmp && tmp <= r {
				result++
			}
		}
	}

	return result
}

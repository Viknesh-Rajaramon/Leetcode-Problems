package main

func maxEqualAdjacentPairs(nums []int) int {
	type Pair struct {
		u, v int
	}

	result, n, base, count := 0, len(nums), 0, make(map[Pair]int)
	for i := range n - 1 {
		if nums[i] == nums[i+1] {
			base++
		} else {
			p := Pair{min(nums[i], nums[i+1]), max(nums[i], nums[i+1])}
			count[p]++
			result = max(result, count[p])
		}
	}

	return base + result
}

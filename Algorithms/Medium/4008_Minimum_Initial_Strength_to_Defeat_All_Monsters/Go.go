package main

func minInitialStrength(monsters []int, boosts [][]int) int64 {
	n := len(monsters)
	diff, bonus := make([]int, n+1), make([]int, n)
	for _, boost := range boosts {
		diff[boost[0]] += boost[2]
		diff[boost[1]+1] -= boost[2]
	}

	bonus[0] = diff[0]
	for i := 1; i < n; i++ {
		bonus[i] = bonus[i-1] + diff[i]
	}

	result := int64(0)
	for i := n - 1; i >= 0; i-- {
		if result == 0 {
			result = int64(max(0, monsters[i]-bonus[i]))
		} else {
			result += int64(monsters[i])
		}
	}

	return result
}

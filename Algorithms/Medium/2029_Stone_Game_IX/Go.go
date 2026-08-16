package main

func stoneGameIX(stones []int) bool {
	count := make([]int, 3)
	for _, val := range stones {
		count[val%3]++
	}

	if count[0]%2 == 0 {
		return count[1] >= 1 && count[2] >= 1
	}

	return count[1]-count[2] > 2 || count[2]-count[1] > 2
}

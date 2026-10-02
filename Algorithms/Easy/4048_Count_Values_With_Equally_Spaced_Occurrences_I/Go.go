package main

func countSpecialIntegers(nums []int) int {
	pos := make(map[int][]int)
	for i, num := range nums {
		pos[num] = append(pos[num], i)
	}

	result := 0
	for _, indices := range pos {
		if len(indices) == 3 && 2*indices[1] == indices[0]+indices[2] {
			result++
		}
	}

	return result
}

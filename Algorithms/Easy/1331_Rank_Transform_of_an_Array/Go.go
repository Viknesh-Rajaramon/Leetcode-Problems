package main

import (
	"sort"
)

func arrayRankTransform(arr []int) []int {
	nums := append([]int(nil), arr...)
	sort.Ints(nums)
	ranks, rank := make(map[int]int), 1
	for _, num := range nums {
		if _, exists := ranks[num]; !exists {
			ranks[num] = rank
			rank++
		}
	}

	for i, num := range arr {
		arr[i] = ranks[num]
	}

	return arr
}

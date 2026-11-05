package main

import (
	"sort"
)

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	sort.Ints(arr2)
	result := 0
	for _, num := range arr1 {
		idx := sort.Search(len(arr2), func(i int) bool {
			return arr2[i] >= num-d
		})

		if idx == len(arr2) || arr2[idx] > num+d {
			result++
		}
	}

	return result
}

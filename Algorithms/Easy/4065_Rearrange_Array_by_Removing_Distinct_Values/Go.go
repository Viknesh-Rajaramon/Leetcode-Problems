package main

import (
	"sort"
)

func rearrangeArray(nums []int) []int {
	result, freq := make([]int, 0), make(map[int]int)
	for _, num := range nums {
		freq[num]++
	}

	keys, max_freq := make([]int, 0), 0
	for key, value := range freq {
		keys = append(keys, key)
		max_freq = max(max_freq, value)
	}

	sort.Ints(keys)
	for i := 1; i <= max_freq; i++ {
		for _, key := range keys {
			if freq[key] >= i {
				result = append(result, key)
			}
		}
	}

	return result
}

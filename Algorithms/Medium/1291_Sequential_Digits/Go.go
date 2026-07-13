package main

import (
	"sort"
)

func sequentialDigits(low int, high int) []int {
	result := make([]int, 0)

	var find func(n int)
	find = func(n int) {
		if n > high {
			return
		}

		if n >= low && n <= high {
			result = append(result, n)
		}

		s := n % 10
		if s < 9 {
			find(n*10 + s + 1)
		}
	}

	for i := 1; i < 10; i++ {
		find(i)
	}

	sort.Ints(result)
	return result
}

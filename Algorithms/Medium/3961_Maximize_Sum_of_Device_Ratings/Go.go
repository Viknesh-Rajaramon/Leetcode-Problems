package main

import (
	"math"
	"sort"
)

func maxRatings(units [][]int) int64 {
	result, n, global_min, sec_min := int64(0), len(units[0]), math.MaxInt, math.MaxInt
	for _, unit := range units {
		sort.Ints(unit)
		global_min = min(global_min, unit[0])
		if n > 1 {
			sec_min = min(sec_min, unit[1])
			result += int64(unit[1])
		} else {
			sec_min = min(sec_min, unit[0])
			result += int64(unit[0])
		}
	}

	return result - int64(sec_min) + int64(global_min)
}

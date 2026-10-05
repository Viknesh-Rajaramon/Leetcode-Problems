package main

import (
	"math"
	"slices"
	"sort"
	"strconv"
)

func minOperations(nums []int) int64 {
	even, odd := make([]int, 0), make([]int, 0)
	for length := 1; length <= len(strconv.Itoa(slices.Max(nums))); length++ {
		half := (length + 1) / 2
		start, end := int(math.Pow10(half-1)), int(math.Pow10(half))
		for x := start; x < end; x++ {
			s := strconv.Itoa(x)
			p_str := s
			if length%2 == 1 {
				for i := len(s) - 2; i >= 0; i-- {
					p_str += string(s[i])
				}
			} else {
				for i := len(s) - 1; i >= 0; i-- {
					p_str += string(s[i])
				}
			}

			p, _ := strconv.Atoi(p_str)
			if p%2 == 1 {
				odd = append(odd, p)
			} else {
				even = append(even, p)
			}
		}
	}

	sort.Ints(even)
	sort.Ints(odd)

	result := int64(0)
	for _, num := range nums {
		var arr []int
		if num%2 == 0 {
			arr = even
		} else {
			arr = odd
		}

		pos := sort.SearchInts(arr, num)
		best := int64(math.MaxInt64)
		if pos < len(arr) {
			best = min(best, int64(arr[pos]-num))
		}

		if pos > 0 {
			best = min(best, int64(num-arr[pos-1]))
		}

		result += best / 2
	}

	return result
}

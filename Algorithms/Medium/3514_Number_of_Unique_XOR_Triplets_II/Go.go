package main

import (
	"math/bits"
	"slices"
)

func uniqueXorTriplets(nums []int) int {
	pairs, triplets := map[int]struct{}{0: struct{}{}}, make(map[int]struct{})
	for _, num := range nums {
		triplets[num] = struct{}{}
	}

	k := 1 << bits.Len(uint(slices.Max(nums)))
	for len(nums) > 0 {
		num := nums[len(nums)-1]
		nums = nums[:len(nums)-1]
		for x := range pairs {
			triplets[num^x] = struct{}{}
		}

		for _, x := range nums {
			pairs[num^x] = struct{}{}
		}

		if len(triplets) == k {
			return k
		}
	}

	return len(triplets)
}

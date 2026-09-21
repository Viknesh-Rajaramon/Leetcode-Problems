package main

import (
	"sort"
)

func minPrice(prices []int, discounts []int) float64 {
	sort.Slice(prices, func(i, j int) bool {
		return prices[i] > prices[j]
	})

	sort.Slice(discounts, func(i, j int) bool {
		return discounts[i] > discounts[j]
	})

	result := 0
	for i := 0; i < len(prices); i++ {
		if i < len(discounts) {
			result += prices[i] * (100 - discounts[i])
		} else {
			result += prices[i] * 100
		}
	}

	return float64(result) / 100
}

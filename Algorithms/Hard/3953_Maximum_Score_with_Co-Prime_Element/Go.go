package main

import (
	"math"
)

func cal_spf(spf []int) {
	for i := 0; i <= 100000; i++ {
		spf[i] = i
	}

	for i := 2; i <= 100000; i++ {
		if spf[i] != i {
			continue
		}
		for j := i * i; j <= 100000; j += i {
			if spf[j] == j {
				spf[j] = i
			}
		}
	}
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxScore(nums []int, maxVal int) int {
	n := len(nums)
	spf := make([]int, 100001)
	cal_spf(spf)

	maxi := 0
	for _, v := range nums {
		if v > maxi {
			maxi = v
		}
	}

	mpp := make([]int, 100001)
	for _, v := range nums {
		mpp[v]++
	}

	div := make([]int, 100001)
	div[1] = n
	for i := 2; i <= 100000; i++ {
		for j := i; j <= 100000; j += i {
			div[i] += mpp[j]
		}
	}

	result := math.MinInt32
	limit := max(maxVal, maxi)
	for x := 1; x <= limit; x++ {
		if mpp[x] == 0 && x > maxVal {
			continue
		}

		temp := x
		vec := []int{}
		for temp > 1 {
			p := spf[temp]
			vec = append(vec, p)
			for temp%p == 0 {
				temp /= p
			}
		}

		siz := len(vec)
		total := 0
		subsets := 1 << siz
		for i := 1; i < subsets; i++ {
			mul := 1
			num := 0
			for j := 0; j < siz; j++ {
				if (i & (1 << j)) != 0 {
					mul *= vec[j]
					num++
				}
			}

			if num%2 == 0 {
				total -= div[mul]
			} else {
				total += div[mul]
			}
		}

		var cost int
		if mpp[x] == 0 {
			if total < 1 {
				cost = 1
			} else {
				cost = total
			}
		} else {
			if x == 1 {
				cost = 0
			} else {
				cost = total - 1
			}
		}

		if x-cost > result {
			result = x - cost
		}
	}

	return result
}

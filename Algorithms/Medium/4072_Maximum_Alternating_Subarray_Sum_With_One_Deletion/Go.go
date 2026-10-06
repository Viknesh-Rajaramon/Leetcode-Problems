package main

import (
	"math"
)

func maxAlternatingSum(nums []int) int64 {
	result, p_0, m_0, p_1, m_1 := int64(math.MinInt64), int64(math.MinInt64), int64(math.MinInt64), int64(math.MinInt64), int64(math.MinInt64)
	for _, n := range nums {
		num := int64(n)
		np_0, nm_0, np_1, nm_1 := num, int64(math.MinInt64), p_0, m_0
		if m_0 != math.MinInt64 {
			np_0 = max(np_0, m_0+num)
		}

		if p_0 != math.MinInt64 {
			nm_0 = p_0 - num
		}

		if m_1 != math.MinInt64 {
			np_1 = max(np_1, m_1+num)
		}

		if p_1 != math.MinInt64 {
			nm_1 = max(nm_1, p_1-num)
		}

		p_0, p_1, m_0, m_1 = np_0, np_1, nm_0, nm_1
		result = max(result, p_1, m_1, m_0, p_0)
	}

	return result
}

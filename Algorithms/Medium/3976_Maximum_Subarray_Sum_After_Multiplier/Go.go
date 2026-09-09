package main

import (
	"math"
)

func maxSubarraySum(nums []int, k int) int64 {
	solve := func(mul bool) int64 {
		NEG_INF := int64(math.MinInt64)
		result, dp_0, dp_1, dp_2 := NEG_INF, NEG_INF, NEG_INF, NEG_INF
		for _, num := range nums {
			x := int64(num)
			var y int64
			if mul {
				y = x * int64(k)
			} else {
				if num >= 0 {
					y = x / int64(k)
				} else {
					y = -((-x) / int64(k))
				}
			}

			d_0, d_1, d_2 := x, y, NEG_INF
			if dp_0 != NEG_INF {
				d_0 = max(d_0, dp_0+x)
				d_1 = max(d_1, dp_0+y)
			}

			if dp_1 != NEG_INF {
				d_1 = max(d_1, dp_1+y)
				d_2 = max(d_2, dp_1+x)
			}

			if dp_2 != NEG_INF {
				d_2 = max(d_2, dp_2+x)
			}

			dp_0, dp_1, dp_2 = d_0, d_1, d_2
			result = max(result, dp_1, dp_2)
		}

		return result
	}

	return max(solve(true), solve(false))
}

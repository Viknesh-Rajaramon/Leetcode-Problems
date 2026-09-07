package main

import (
	"math"
)

func maximumSum(nums []int, m int, l int, r int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(nums[i])
	}

	type Triplet struct {
		pos int
		val int64
		cnt int
	}

	best_single := func() int64 {
		queue, best := make([]Triplet, 0), int64(math.MinInt64)
		for i := 1; i <= n; i++ {
			j := i - l
			if j >= 0 {
				for len(queue) > 0 && queue[len(queue)-1].val >= prefix[j] {
					queue = queue[:len(queue)-1]
				}

				queue = append(queue, Triplet{pos: j, val: prefix[j], cnt: 0})
			}

			for len(queue) > 0 && queue[0].pos < i-r {
				queue = queue[1:]
			}

			if len(queue) > 0 {
				best = max(best, prefix[i]-queue[0].val)
			}
		}

		return best
	}

	single := best_single()
	var check func(cost int) (int64, int)
	check = func(cost int) (int64, int) {
		dp_val, dp_cnt, queue := make([]int64, n+1), make([]int, n+1), make([]Triplet, 0)
		for i := 1; i <= n; i++ {
			j := i - l
			if j >= 0 {
				val, cnt := dp_val[j]-prefix[j], dp_cnt[j]
				for len(queue) > 0 && (queue[len(queue)-1].val < val || (queue[len(queue)-1].val == val && queue[len(queue)-1].cnt >= cnt)) {
					queue = queue[:len(queue)-1]
				}

				queue = append(queue, Triplet{pos: j, val: val, cnt: cnt})
			}

			for len(queue) > 0 && queue[0].pos < i-r {
				queue = queue[1:]
			}

			dp_val[i], dp_cnt[i] = dp_val[i-1], dp_cnt[i-1]
			if len(queue) > 0 {
				val, cnt := prefix[i]-int64(cost)+queue[0].val, queue[0].cnt+1
				if val > dp_val[i] || (val == dp_val[i] && cnt < dp_cnt[i]) {
					dp_val[i], dp_cnt[i] = val, cnt
				}
			}
		}

		return dp_val[n], dp_cnt[n]
	}

	val, cnt := check(0)
	if cnt <= m {
		if cnt > 0 {
			return val
		}

		return single
	}

	low, high := 0, 1
	for _, num := range nums {
		high += max(num, -num)
	}

	for low < high {
		mid := (low + high) >> 1
		val, cnt = check(mid)
		if cnt > m {
			low = mid + 1
		} else {
			high = mid
		}
	}

	val, cnt = check(low)
	return max(single, val+int64(low*m))
}

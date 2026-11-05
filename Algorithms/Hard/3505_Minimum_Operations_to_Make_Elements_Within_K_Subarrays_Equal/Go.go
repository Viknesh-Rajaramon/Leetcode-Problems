package main

import (
	"container/heap"
	"math"
	"sort"
)

type State struct {
	num int
	idx int
}

type PQ []State

func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i, j int) bool {
	return p[i].num < p[j].num || (p[i].num == p[j].num && p[i].idx < p[j].idx)
}
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(State)) }
func (p *PQ) Pop() interface{} {
	old := *p
	n := len(old)
	item := old[n-1]
	*p = old[:n-1]
	return item
}

func minOperations(nums []int, x int, k int) int64 {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	n, l_size, r_size, init := len(nums), x/2, x-x/2, make([]State, x)
	for i := range x {
		init[i] = State{nums[i], i}
	}

	sort.Slice(init, func(i, j int) bool {
		return init[i].num < init[j].num || (init[i].num == init[j].num && init[i].idx < init[j].idx)
	})

	mid, left, right, cost := init[l_size].num, &PQ{}, &PQ{}, int64(0)
	heap.Init(left)
	heap.Init(right)
	for j := range x {
		num, i := init[j].num, init[j].idx
		cost += int64(abs(num - mid))
		if j < l_size {
			heap.Push(left, State{-num, -i})
		} else {
			heap.Push(right, State{num, i})
		}
	}

	costs := make([]int64, x)
	for i := range x {
		costs[i] = int64(math.MaxInt64)
	}

	costs = append(costs, cost)
	for i := x; i < n; i++ {
		cost += int64(abs(nums[i]-mid) - abs(nums[i-x]-mid))
		if nums[i-x] < (*right)[0].num || (nums[i-x] == (*right)[0].num && i-x < (*right)[0].idx) {
			for left.Len() > 0 && -(*left)[0].idx <= i-x {
				heap.Pop(left)
			}

			if nums[i] < (*right)[0].num {
				heap.Push(left, State{-nums[i], -i})
			} else {
				pop_right := heap.Pop(right).(State)
				for right.Len() > 0 && (*right)[0].idx <= i-x {
					heap.Pop(right)
				}

				heap.Push(left, State{-pop_right.num, -pop_right.idx})
				heap.Push(right, State{nums[i], i})

				cost += int64((l_size - r_size) * abs((*right)[0].num-mid))
				mid = (*right)[0].num
			}
		} else {
			for right.Len() > 0 && (*right)[0].idx <= i-x {
				heap.Pop(right)
			}

			if nums[i] >= -(*left)[0].num {
				heap.Push(right, State{nums[i], i})
				if mid < (*right)[0].num {
					cost += int64((l_size - r_size) * abs((*right)[0].num-mid))
				} else {
					cost += int64((r_size - l_size - 2) * abs((*right)[0].num-mid))
				}

				mid = (*right)[0].num
			} else {
				pop_left := heap.Pop(left).(State)
				pop_left.num, pop_left.idx = -pop_left.num, -pop_left.idx
				for left.Len() > 0 && -(*left)[0].idx <= i-x {
					heap.Pop(left)
				}

				heap.Push(left, State{-nums[i], -i})
				heap.Push(right, State{pop_left.num, pop_left.idx})

				cost += int64((r_size - l_size - 2) * abs(mid-pop_left.num))
				mid = pop_left.num
			}
		}

		costs = append(costs, cost)
	}

	dp := []int64{math.MaxInt64}
	for i := range n {
		dp = append(dp, min(dp[len(dp)-1], costs[i+1]))
	}

	for i := 1; i < k; i++ {
		new_dp := make([]int64, x)
		for j := range x {
			new_dp[j] = int64(math.MaxInt64)
		}

		for j := x; j <= n; j++ {
			best := new_dp[len(new_dp)-1]
			if dp[j-x] != math.MaxInt64 && costs[j] != math.MaxInt64 {
				best = min(best, dp[j-x]+costs[j])
			}

			new_dp = append(new_dp, best)
		}

		dp = new_dp
	}

	return dp[len(dp)-1]
}

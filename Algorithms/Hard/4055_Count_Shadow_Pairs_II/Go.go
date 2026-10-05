package main

import (
	"sort"
)

type Counter struct {
	temp   []int
	stack  []int
	caps   []int
	starts []int
	size   int
}

func (c *Counter) count(sequence []int, low, high int) int {
	if len(sequence) < 2 || low == high {
		return 0
	}

	result, mid, left_count := 0, (low+high)>>1, 0
	stack, caps, starts := c.stack[:0], c.caps[:0], c.starts[:0]
	for _, x := range sequence {
		if x <= mid {
			left_count++
			for len(stack) > 0 && stack[len(stack)-1] < x {
				stack = stack[:len(stack)-1]
			}

			size := len(stack)
			for len(starts) > 0 && starts[len(starts)-1] >= size {
				starts = starts[:len(starts)-1]
				caps = caps[:len(caps)-1]
			}

			stack = append(stack, x)
			if len(caps) == 0 || caps[len(caps)-1] != c.size {
				caps = append(caps, c.size)
				starts = append(starts, size)
			}
		} else {
			p := sort.SearchInts(caps, x)
			if p == len(caps) {
				continue
			}

			start := starts[p]
			result += len(stack) - start
			caps = append(caps[:p], x)
			starts = append(starts[:p], start)
		}
	}

	left, right := 0, left_count
	for _, x := range sequence {
		if x <= mid {
			c.temp[left] = x
			left++
		} else {
			c.temp[right] = x
			right++
		}
	}

	copy(sequence, c.temp[:len(sequence)])
	result += c.count(sequence[:left_count], low, mid)
	result += c.count(sequence[left_count:], mid+1, high)
	return result
}

func shadowPairs(nums []int) int {
	values := append([]int{}, nums...)
	sort.Ints(values)

	n := 0
	for _, x := range values {
		if n == 0 || values[n-1] != x {
			values[n] = x
			n++
		}
	}

	values = values[:n]
	if n == 1 {
		return 0
	}

	ranks := make([]int, len(nums))
	for i, value := range nums {
		ranks[i] = sort.SearchInts(values, value)
	}

	counter := Counter{
		temp:   make([]int, len(nums)),
		stack:  make([]int, 0, len(nums)),
		caps:   make([]int, 0, len(nums)),
		starts: make([]int, 0, len(nums)),
		size:   n,
	}

	return counter.count(ranks, 0, n-1)
}

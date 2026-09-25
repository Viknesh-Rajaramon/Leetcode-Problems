package main

import (
	"math"
	"sort"
)

type Mo struct {
	freq     map[int]int
	odd_freq map[int]bool
	k        int
}

func NewMo(k int) *Mo {
	return &Mo{
		freq:     make(map[int]int),
		odd_freq: make(map[int]bool),
		k:        k,
	}
}

func (mo *Mo) add(num int) {
	mo.freq[num]++
	if mo.odd_freq[num] {
		delete(mo.odd_freq, num)
	} else {
		mo.odd_freq[num] = true
	}
}

func (mo *Mo) remove(num int) {
	mo.freq[num]--
	if mo.freq[num] == 0 {
		delete(mo.freq, num)
	}

	if mo.odd_freq[num] {
		delete(mo.odd_freq, num)
	} else {
		mo.odd_freq[num] = true
	}
}

func (mo *Mo) check() bool {
	return len(mo.freq) == mo.k && len(mo.odd_freq) == 0
}

type Query struct {
	l, r, i int
}

func validSubarrays(nums []int, k int, queries [][]int) []bool {
	q, block_size := len(queries), int(math.Max(1, math.Sqrt(float64(len(nums)))))
	qs := make([]Query, q)
	for i, query := range queries {
		qs[i] = Query{l: query[0], r: query[1], i: i}
	}

	sort.Slice(qs, func(i, j int) bool {
		a, b := qs[i].l/block_size, qs[j].l/block_size
		if a != b {
			return a < b
		}

		if a%2 == 0 {
			return qs[i].r < qs[j].r
		}

		return qs[i].r > qs[j].r
	})

	result, l, r := make([]bool, q), 0, -1
	mo := NewMo(k)
	for _, query := range qs {
		start, end, i := query.l, query.r, query.i
		for l > start {
			l--
			mo.add(nums[l])
		}

		for r < end {
			r++
			mo.add(nums[r])
		}

		for l < start {
			mo.remove(nums[l])
			l++
		}

		for r > end {
			mo.remove(nums[r])
			r--
		}

		result[i] = mo.check()
	}

	return result
}

package main

import (
	"math/bits"
	"sort"
)

type SparseTable struct {
	st [][]int
}

func NewSparseTable(data []int) *SparseTable {
	st := &SparseTable{}
	st.st = append(st.st, append([]int{}, data...))
	i, n := 1, len(st.st[0])
	for 2*i <= n+1 {
		pre := st.st[len(st.st)-1]
		curr := make([]int, n+1-2*i)
		for j := 0; j <= n-2*i; j++ {
			curr[j] = max(pre[j], pre[j+i])
		}

		st.st = append(st.st, curr)
		i <<= 1
	}

	return st
}

func (st *SparseTable) query(begin, end int) int {
	if begin > end {
		return 0
	}

	lg := bits.Len(uint(end-begin+1)) - 1
	return max(st.st[lg][begin], st.st[lg][end+1-(1<<lg)])
}

func maxActiveSectionsAfterTrade(s string, queries [][]int) []int {
	n, count := len(s), 0
	for _, c := range s {
		if c == '1' {
			count++
		}
	}

	zero_blocks, left, right, i := make([]int, 0), make([]int, 0), make([]int, 0), 0
	for i < n {
		st := i
		for i < n && s[i] == s[st] {
			i++
		}

		if s[st] == '0' {
			zero_blocks = append(zero_blocks, i-st)
			left = append(left, st)
			right = append(right, i-1)
		}
	}

	m := len(zero_blocks)
	if m < 2 {
		result := make([]int, len(queries))
		for i := range result {
			result[i] = count
		}

		return result
	}

	tmp_sum := make([]int, m-1)
	for i := 0; i < m-1; i++ {
		tmp_sum[i] = zero_blocks[i] + zero_blocks[i+1]
	}

	result, st := make([]int, 0), NewSparseTable(tmp_sum)
	for _, q := range queries {
		i := sort.Search(len(right), func(k int) bool {
			return right[k] >= q[0]
		})

		j := sort.Search(len(left), func(k int) bool {
			return left[k] > q[1]
		}) - 1

		if i > m-1 || j < 0 || i >= j {
			result = append(result, count)
			continue
		}

		first, last := right[i]+1-max(left[i], q[0]), min(right[j], q[1])+1-left[j]
		if i+1 == j {
			result = append(result, count+first+last)
			continue
		}

		best := max(first+zero_blocks[i+1], zero_blocks[j-1]+last, st.query(i+1, j-2))
		result = append(result, count+best)
	}

	return result
}

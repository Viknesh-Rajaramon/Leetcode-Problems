package main

type FenwickTree struct {
	n   int
	bit []int
}

func NewFenwickTree(n int) *FenwickTree {
	return &FenwickTree{
		n:   n,
		bit: make([]int, n+1),
	}
}

func (ft *FenwickTree) update(idx, val int) {
	for idx <= ft.n {
		ft.bit[idx] += val
		idx += idx & -idx
	}
}

func (ft *FenwickTree) query(idx int) int {
	res := 0
	for idx > 0 {
		res += ft.bit[idx]
		idx -= idx & -idx
	}

	return res
}

func minOperations(nums []int, locked []int, k int) int {
	n, blocks, start, max_so_far := len(nums), make([][]int, 0), 0, 0
	for i := range n {
		max_so_far = max(max_so_far, nums[i])
		if max_so_far == i+1 {
			blocks = append(blocks, []int{start, i})
			start = i + 1
		}
	}

	result := 0
	for _, block := range blocks {
		start, end := block[0], block[1]
		if start == end {
			continue
		}

		for i := start; i <= end; i++ {
			if locked[i] == 1 {
				result++
			}
		}
	}

	if result > k {
		return -1
	}

	ft := NewFenwickTree(n)
	for i := n - 1; i >= 0; i-- {
		result += ft.query(nums[i] - 1)
		ft.update(nums[i], 1)
	}

	return result
}

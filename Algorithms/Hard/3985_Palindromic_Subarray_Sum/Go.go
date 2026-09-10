package main

import (
	"math"
)

func getSum(nums []int) int64 {
	type Node struct {
		len_, link int
		next       map[int]int
	}

	n := len(nums)
	prefix := make([]int, n+1)
	for i := range n {
		prefix[i+1] = prefix[i] + nums[i]
	}

	result, last := int64(math.MinInt64), 0
	tree := []Node{Node{0, 1, make(map[int]int)}, Node{-1, 1, make(map[int]int)}}
	walk := func(node int, i int) int {
		for i-1-tree[node].len_ < 0 || nums[i-1-tree[node].len_] != nums[i] {
			node = tree[node].link
		}

		return node
	}

	for i := range n {
		curr := walk(last, i)
		if _, exists := tree[curr].next[nums[i]]; !exists {
			link, len_ := walk(tree[curr].link, i), tree[curr].len_+2
			temp := 0
			if tree[curr].len_ != -1 {
				temp = tree[link].next[nums[i]]
			}

			tree = append(tree, Node{len_, temp, make(map[int]int)})
			tree[curr].next[nums[i]] = len(tree) - 1
			result = max(result, int64(prefix[i+1]-prefix[i+1-len_]))
		}

		last = tree[curr].next[nums[i]]
	}

	return result
}

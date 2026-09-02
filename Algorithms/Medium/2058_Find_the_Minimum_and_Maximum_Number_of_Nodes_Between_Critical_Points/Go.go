package main

import (
	"math"
)

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func nodesBetweenCriticalPoints(head *ListNode) []int {
	min_dist, prev, curr, first_idx, prev_idx, curr_idx := math.MaxInt, head, head.Next, 0, 0, 1
	for curr.Next != nil {
		if (curr.Val < prev.Val && curr.Val < curr.Next.Val) || (curr.Val > prev.Val && curr.Val > curr.Next.Val) {
			if prev_idx == 0 {
				first_idx = curr_idx
			} else {
				min_dist = min(min_dist, curr_idx-prev_idx)
			}

			prev_idx = curr_idx
		}

		curr_idx++
		prev, curr = curr, curr.Next
	}

	if min_dist == math.MaxInt {
		return []int{-1, -1}
	}

	return []int{min_dist, prev_idx - first_idx}
}

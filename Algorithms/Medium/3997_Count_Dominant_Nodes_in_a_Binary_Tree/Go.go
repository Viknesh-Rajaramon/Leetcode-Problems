package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countDominantNodes(root *TreeNode) int {
	result := 0
	var postorder func(node *TreeNode) int
	postorder = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		left_max := postorder(node.Left)
		right_max := postorder(node.Right)
		if node.Val >= left_max && node.Val >= right_max {
			result++
			return node.Val
		}

		return max(left_max, right_max)
	}

	postorder(root)
	return result
}

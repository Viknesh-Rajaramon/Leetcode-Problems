package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfSubtree(root *TreeNode) int {
	result := 0
	var dfs func(node *TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}

		left_sum, left_nodes := dfs(node.Left)
		right_sum, right_nodes := dfs(node.Right)

		sum_, nodes_ := left_sum+right_sum+node.Val, left_nodes+right_nodes+1
		if sum_/nodes_ == node.Val {
			result++
		}

		return sum_, nodes_
	}

	dfs(root)
	return result
}

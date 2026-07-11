package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func createBinaryTree(descriptions [][]int) *TreeNode {
	nodes := make(map[int]*TreeNode)
	for _, d := range descriptions {
		child := d[1]
		if _, exists := nodes[child]; !exists {
			nodes[child] = &TreeNode{Val: child}
		}
	}

	var root *TreeNode
	for _, d := range descriptions {
		parent := d[0]
		child := d[1]
		isLeft := d[2]

		if _, exists := nodes[parent]; !exists {
			root = &TreeNode{Val: parent}
			nodes[parent] = root
		}

		if isLeft == 1 {
			nodes[parent].Left = nodes[child]
		} else {
			nodes[parent].Right = nodes[child]
		}
	}

	return root
}

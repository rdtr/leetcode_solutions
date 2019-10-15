package main

func diameterOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	doDiameterOfBinaryTree(root, &res)
	return res
}

func doDiameterOfBinaryTree(node *TreeNode, res *int) int {
	if node.Left == nil && node.Right == nil {
		*res = max(*res, 0)
		return 0
	} else if node.Left == nil && node.Right != nil {
		h := doDiameterOfBinaryTree(node.Right, res)
		*res = max(*res, h+1)
		return h + 1
	} else if node.Left != nil && node.Right == nil {
		h := doDiameterOfBinaryTree(node.Left, res)
		*res = max(*res, h+1)
		return h + 1
	} else {
		hl, hr := doDiameterOfBinaryTree(node.Left, res), doDiameterOfBinaryTree(node.Right, res)
		*res = max(*res, hl+hr+2)
		return max(hl, hr) + 1
	}
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

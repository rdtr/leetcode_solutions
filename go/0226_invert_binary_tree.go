package main

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	root.Right, root.Left = invertTree(root.Left), invertTree(root.Right)
	return root
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	que := []*TreeNode{root}
	for len(que) > 0 {
		node := que[0]
		que = que[1:]

		node.Left, node.Right = node.Right, node.Left
		if node.Left != nil {
			que = append(que, node.Left)
		}
		if node.Right != nil {
			que = append(que, node.Right)
		}
	}
	return root
}

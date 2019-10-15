package main

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	switch {
	case root1 == nil && root2 == nil:
		return true
	case root1 != nil && root2 == nil, root1 == nil && root2 != nil:
		return false
	default:
		var res1, res2 []int
		dfs(root1, &res1)
		dfs(root2, &res2)

		if len(res1) != len(res2) {
			return false
		}
		for i := 0; i < len(res1); i++ {
			if res1[i] != res2[i] {
				return false
			}
		}
		return true
	}
}

func dfs(node *TreeNode, res *[]int) {
	if node.Left == nil && node.Right == nil {
		*res = append(*res, node.Val)
		return
	}
	if node.Left != nil {
		dfs(node.Left, res)
	}
	if node.Right != nil {
		dfs(node.Right, res)
	}
}

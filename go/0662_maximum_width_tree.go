/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func widthOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	} else if root.Left == nil && root.Right == nil {
		return 1
	}

	q := []*TreeNode{&TreeNode{0, root.Left, root.Right}}
	var res int
	for {
		qlen := len(q)
		if qlen == 0 {
			break
		}

		var mostLeft, mostRight *int
		for i := 0; i < qlen; i++ {
			node := q[0]
			q = q[1:]
			if node.Left != nil {
				newVal := node.Val * 2
				q = append(q, &TreeNode{newVal, node.Left.Left, node.Left.Right})
				if mostLeft == nil || *mostLeft > newVal {
					mostLeft = &newVal
				}
				if mostRight == nil || *mostRight < newVal {
					mostRight = &newVal
				}
			}
			if node.Right != nil {
				newVal := node.Val*2 + 1
				q = append(q, &TreeNode{newVal, node.Right.Left, node.Right.Right})
				if mostLeft == nil || *mostLeft > newVal {
					mostLeft = &newVal
				}
				if mostRight == nil || *mostRight < newVal {
					mostRight = &newVal
				}
			}
		}

		switch {
		case mostLeft != nil && mostRight == nil, mostLeft == nil && mostRight != nil:
			if res < 1 {
				res = 1
			}
		case mostLeft != nil && mostRight != nil:
			if distance := *mostRight - *mostLeft + 1; distance > res {
				res = distance
			}
		}
	}
	return res
}
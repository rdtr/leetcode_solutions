/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	queue := []*TreeNode{root}
	var res [][]int
	leftToRight := false
	for {
		qlen := len(queue)
		if qlen == 0 {
			break
		}

		var arr []int
		for i := qlen - 1; i >= 0; i-- {
			node := queue[0]
			arr = append(arr, node.Val)

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			queue = queue[1:]
		}

		if leftToRight {
			reverse(arr)
		}
		res = append(res, arr)
		leftToRight = !leftToRight
	}
	return res
}

func reverse(list []int) {
	if len(list) > 0 {
		for i := 0; i < len(list)/2; i++ {
			list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
		}
	}
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	lqueue, rqueue := []*TreeNode{root}, []*TreeNode{root}
	var res [][]int
	leftToRight := true
	for {
		lqlen, rqlen := len(lqueue), len(rqueue)
		if lqlen == 0 || rqlen == 0 {
			break
		}

		var arr []int
		for i := 0; i < lqlen; i++ {
			lnode, rnode := lqueue[0], rqueue[0]
			if lnode.Left != nil {
				lqueue = append(lqueue, lnode.Left)
			}
			if lnode.Right != nil {
				lqueue = append(lqueue, lnode.Right)
			}

			if rnode.Right != nil {
				rqueue = append(rqueue, rnode.Right)
			}
			if rnode.Left != nil {
				rqueue = append(rqueue, rnode.Left)
			}
			lqueue, rqueue = lqueue[1:], rqueue[1:]

			if leftToRight {
				arr = append(arr, lnode.Val)
			} else {
				arr = append(arr, rnode.Val)
			}
		}
		res = append(res, arr)
		leftToRight = !leftToRight
	}
	return res
}
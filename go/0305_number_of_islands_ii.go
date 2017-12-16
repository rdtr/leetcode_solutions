func numIslands2(m int, n int, positions [][]int) []int {
	grid := make([][]int, m)                // grid representation
	treeGrid := make([][]*UnionFindTree, m) // to be able to access each tree node by x and y coordinate
	for i := 0; i < m; i++ {
		grid[i] = make([]int, n)
		treeGrid[i] = make([]*UnionFindTree, n)
	}

	var res []int
	count := 0
	for _, pos := range positions {
		x, y := pos[0], pos[1]

		grid[x][y] = 1
		t := &UnionFindTree{M: x, N: y}
		treeGrid[x][y] = t

		count++
		var leftRoot, rightRoot, topRoot, bottomRoot *UnionFindTree
		// check left
		if x > 0 && grid[x-1][y] == 1 {
			leftRoot = Find(treeGrid[x-1][y])

			Union(t, leftRoot)
			count--
		}

		// check right
		if x < m-1 && grid[x+1][y] == 1 {
			rightRoot = Find(treeGrid[x+1][y])

			if rightRoot != t {
				count--
				Union(t, rightRoot)
			}
		}

		// check bottom
		if y > 0 && grid[x][y-1] == 1 {
			bottomRoot = Find(treeGrid[x][y-1])

			if bottomRoot != t {
				count--
				Union(t, bottomRoot)
			}
		}

		// check top
		if y < n-1 && grid[x][y+1] == 1 {
			topRoot = Find(treeGrid[x][y+1])

			if topRoot != t {
				count--
				Union(t, topRoot)
			}
		}

		res = append(res, count)
	}
	return res
}

type UnionFindTree struct {
	Parent *UnionFindTree
	M      int
	N      int
}

func Find(t *UnionFindTree) *UnionFindTree {
	if t.Parent == nil {
		return t
	}
	root := Find(t.Parent)

	// restructure a tree to minimize a number of traversal
	t.Parent = root
	return root
}

func Union(t1, t2 *UnionFindTree) {
	t2.Parent = t1
}
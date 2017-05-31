package main

func generate(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	} else if numRows == 1 {
		return [][]int{[]int{1}}
	}

	rows := [][]int{[]int{1}, []int{1, 1}}
	for i := 2; i < numRows; i++ {
		lastRow := rows[len(rows)-1]
		newRow := make([]int, len(lastRow)+1)
		for j := 0; j < len(newRow); j++ {
			if j == 0 || j == len(newRow)-1 {
				newRow[j] = 1
				continue
			}
			newRow[j] = lastRow[j] + lastRow[j-1]
		}
		rows = append(rows, newRow)
	}
	return rows
}

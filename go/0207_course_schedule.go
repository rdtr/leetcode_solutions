func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := buildGraph(prerequisites, numCourses)

	visited := make(map[int]bool)
	curVisited := make(map[int]bool)
	for start, _ := range graph {
		if res := dfs(start, graph, visited, curVisited); !res {
			return false
		}
	}
	return true
}

func dfs(start int, graph map[int][]int, visited map[int]bool, curVisited map[int]bool) bool {
	if val, ok := visited[start]; ok && val {
		return true
	}
	curVisited[start] = true

	neighbors := graph[start]
	for _, neighbor := range neighbors {
		if val, ok := curVisited[neighbor]; ok && val {
			return false
		}
		if res := dfs(neighbor, graph, visited, curVisited); !res {
			return false
		}
	}
	curVisited[start], visited[start] = false, true
	return true
}

// buildGraph returns a graph as {courseID: [requirements courseIDs]} map
// and returns start courses which aren't required by any courses.
func buildGraph(prerequisites [][]int, numCourses int) map[int][]int {
	graph := make(map[int][]int)
	for _, p := range prerequisites {
		if _, ok := graph[p[1]]; ok {
			graph[p[1]] = append(graph[p[1]], p[0])
		} else {
			graph[p[1]] = []int{p[0]}
		}
	}
	return graph
}



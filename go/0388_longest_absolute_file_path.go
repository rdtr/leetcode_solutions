import "strings"

func lengthLongestPath(input string) int {
	res, cache, fileDirs := 0, make(map[int]int), strings.Split(input, "\n")

	for _, fileDir := range fileDirs {
		level := 0
		for fileDir[0] == '\t' {
			level, fileDir = level+1, fileDir[1:]
		}
		if level == 0 {
			if strings.Index(fileDir, ".") != -1 {
				res = len(fileDir)
			} else {
				cache[0] = len(fileDir)
			}
			continue
		}

		if strings.Index(fileDir, ".") != -1 { // file
			if curLen := cache[level-1] + 1 + len(fileDir); curLen > res {
				res = curLen
			}
		} else { // dir
			cache[level] = cache[level-1] + 1 + len(fileDir)
		}
	}
	return res
}

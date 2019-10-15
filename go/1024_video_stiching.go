package main

import "sort"

func videoStitching(clips [][]int, T int) int {
	sort.Slice(clips, func(i, j int) bool {
		if clips[i][0] == clips[j][0] {
			return clips[i][1] < clips[j][1]
		}
		return clips[i][0] < clips[j][0]
	})

	var res [][]int
	for i := 0; i < len(clips); i++ {
		if len(res) == 0 {
			res = append(res, clips[i])
		} else if res[len(res)-1][1] < clips[i][0] {
			return -1
		} else if res[len(res)-1][0] == clips[i][0] {
			res[len(res)-1][1] = clips[i][1]
		} else if res[len(res)-1][1] < clips[i][1] {
			for len(res) > 1 && res[len(res)-2][1] >= clips[i][0] {
				res = res[:len(res)-1]
			}
			res = append(res, clips[i])
		}

		if clips[i][1] >= T {
			break
		}
	}

	if len(res) > 0 && (res[len(res)-1][1] < T || res[0][0] != 0) {
		return -1
	}
	return len(res)
}

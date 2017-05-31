import "sort"

func minMeetingRooms(intervals []Interval) int {
	ilen := len(intervals)
	starts, ends := make([]int, ilen), make([]int, ilen)
	for i, interval := range intervals {
		starts[i], ends[i] = interval.Start, interval.End
	}
	sort.Ints(starts)
	sort.Ints(ends)

	si, ei := 0, 0
	roomNum, roomInUse := 0, 0
	for ei < ilen {
		if si < ilen && starts[si] < ends[ei] { // start event occurs
			if roomNum-roomInUse > 0 { // room available
				roomInUse++
			} else {
				roomNum++
				roomInUse++
			}
			si++
		} else { // end event occurs
			roomInUse--
			ei++
		}
	}
	return roomNum
}
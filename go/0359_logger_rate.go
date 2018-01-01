type Logger struct {
	Cache map[string]*QueItem
	Que   []*QueItem
}

/** Initialize your data structure here. */
func Constructor() Logger {
	c := make(map[string]*QueItem)
	q := make([]*QueItem, 0)
	return Logger{Cache: c, Que: q}
}

/** Returns true if the message should be printed in the given timestamp, otherwise returns false.
  If this method returns false, the message will not be printed.
  The timestamp is in seconds granularity. */
func (this *Logger) ShouldPrintMessage(timestamp int, message string) bool {
	qlen := len(this.Que)
	for i := 0; i < qlen; i++ {
		item := this.Que[0]
		if timestamp-item.Timestamp >= 10 {
			this.Que = this.Que[1:]
			delete(this.Cache, item.Message)
			continue
		}
		break
	}

	if _, ok := this.Cache[message]; !ok {
		item := &QueItem{message, timestamp}
		this.Que = append(this.Que, item)
		this.Cache[item.Message] = item
		return true
	}
	return false
}

type QueItem struct {
	Message   string
	Timestamp int
}
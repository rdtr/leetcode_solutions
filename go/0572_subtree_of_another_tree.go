import (
	"bytes"
	"strconv"
	"strings"
)

func isSubtree(s *TreeNode, t *TreeNode) bool {
	if s == nil {
		return t == nil
	}

	sb, tb := &bytes.Buffer{}, &bytes.Buffer{}
	buildString(s, sb)
	buildString(t, tb)
	sstr, tstr := sb.String(), tb.String()

	if found := strings.Index(sstr, tstr); found != -1 {
		if found == 0 || sstr[found-1] == '|' {
			return true
		}
		sstr = sstr[found+1:]
	}
	return false
}

func buildString(t *TreeNode, b *bytes.Buffer) {
	if t == nil {
		if b.Len() == 0 {
			b.WriteString("_")
		} else {
			b.WriteString("|_")
		}
		return
	}

	valstr := strconv.Itoa(t.Val)
	if b.Len() == 0 {
		b.WriteString(valstr)
	} else {
		b.WriteString("|" + valstr)
	}
	buildString(t.Left, b)
	buildString(t.Right, b)
}


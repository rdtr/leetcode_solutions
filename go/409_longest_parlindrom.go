func longestPalindrome(s string) int {
    m := make(map[byte]int)
    for i := 0; i < len(s); i++ {
        ch := s[i]
        if cnt, ok := m[ch]; ok {
            m[ch] = cnt + 1
        } else {
            m[ch] = 1
        }
    }
    
    res, odd := 0, 0
    for _, cnt := range m {
        if cnt % 2 == 0 {
            res += cnt
            continue
        }
        res += cnt / 2 * 2
        odd = 1
    }
    return res + odd
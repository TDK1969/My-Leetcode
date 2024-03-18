package main

import "fmt"

//--CODE BEGIN--

//lint:ignore U1000 Ignore unused function check
func lengthOfLongestSubstring(s string) int {
	set := make(map[byte]struct{})
	ans := 0
	l, r := 0, 0
	n := len(s)

	for r < n {
		if _, ok := set[s[r]]; ok {
			delete(set, s[l])
			l += 1
		} else {
			set[s[r]] = struct{}{}
			r += 1
			if r-l > ans {
				ans = r - l
			}
		}
	}

	return ans
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: "abcabcbb"
 *TestCase 1: "bbbbb"
 *TestCase 2: "pwwkew"
 *--TESTCASE END--
 */
func main() {
	fmt.Printf("%d", lengthOfLongestSubstring("abcabcbb"))
}

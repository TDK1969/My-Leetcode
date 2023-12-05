/*
 * @Descripttion:
 * @version:
 * @Author: TDK
 * @Date: 2023-11-16 15:02:46
 * @LastEditors: TDK
 * @LastEditTime: 2023-11-16 19:32:56
 */
/* INTRODUCTION
 *日期: 2023-11-16
 *题目: 组合
 *链接: https://leetcode-cn.com/problems/combinations/
 */

package main

// --CODE BEGIN--

//lint:ignore U1000 Ignore unused function check
func combine(n int, k int) [][]int {
	ans := [][]int{}
	cur := []int{}
	var dfs func(start int)
	dfs = func(start int) {
		cur = append(cur, start)
		if len(cur) == k {
			temp := make([]int, len(cur))
			copy(temp, cur)
			ans = append(ans, temp)
		} else {
			for i := start + 1; i < n+2-k+len(cur); i++ {
				dfs(i)
			}
		}
		cur = cur[:len(cur)-1]
	}

	for i := 1; i < n+2-k; i++ {
		dfs(i)
	}
	return ans

}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: 4,2
 *TestCase 1: 1,1
 *--TESTCASE END--
 */
func main() {

}

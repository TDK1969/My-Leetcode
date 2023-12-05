/* INTRODUCTION
 *日期: 2023-11-22
 *题目: 网格中的最小路径代价
 *链接: https://leetcode-cn.com/problems/minimum-path-cost-in-a-grid/
 */

package main

import (
	"fmt"
)

//--CODE BEGIN--

//lint:ignore U1000 Ignore unused function check
func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func minPathCost(grid [][]int, moveCost [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if i == 0 {
				dp[i][j] = grid[i][j]
			} else {
				dp[i][j] = 6000
			}
		}
	}

	for i := 0; i < m-1; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				dp[i+1][k] = min(dp[i+1][k], dp[i][j]+moveCost[grid[i][j]][k]+grid[i+1][k])
			}
		}
	}

	ans := 6000
	for j := 0; j < n; j++ {
		ans = min(ans, dp[m-1][j])
	}

	return ans

}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: {{5,3},{4,0},{2,1}},{{9,8},{1,5},{10,12},{18,6},{2,4},{14,3}}
 *TestCase 1: {{5,1,2},{4,0,3}},{{12,10,15},{20,23,8},{21,7,1},{8,1,13},{9,10,25},{5,3,2}}
 *--TESTCASE END--
 */
func main() {
	fmt.Print(minPathCost([][]int{{5, 3}, {4, 0}, {2, 1}}, [][]int{{9, 8}, {1, 5}, {10, 12}, {18, 6}, {2, 4}, {14, 3}}))
}

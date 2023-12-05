/* INTRODUCTION
 *日期: 2023-11-20
 *题目: 最大子数组和
 *链接: https://leetcode-cn.com/problems/maximum-subarray/
 */

package main

import (
	"fmt"
)

//--CODE BEGIN--

//lint:ignore U1000 Ignore unused function check
func maxSubArray(nums []int) int {
	ans := -10005
	cur := 0
	for _, num := range nums {
		cur += num
		if cur > ans {
			ans = cur
		}
		if cur < 0 {
			cur = 0
		}
	}

	return ans
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: {-2,1,-3,4,-1,2,1,-5,4}
 *TestCase 1: {1}
 *TestCase 2: {5,4,-1,7,8}
 *--TESTCASE END--
 */
func main() {
	fmt.Print(maxSubArray([]int{-1}))
}

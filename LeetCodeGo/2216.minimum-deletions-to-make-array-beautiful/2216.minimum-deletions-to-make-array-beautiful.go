/* INTRODUCTION
 *日期: 2023-11-21
 *题目: 美化数组的最少删除数
 *链接: https://leetcode-cn.com/problems/minimum-deletions-to-make-array-beautiful/
 */

package main

import (
	"fmt"
)

//--CODE BEGIN--

//lint:ignore U1000 Ignore unused function check
func minDeletion(nums []int) int {
	flag := 0
	ans := 0

	for i := 0; i < len(nums)-1; i++ {
		if i&1 == flag && nums[i] == nums[i+1] {
			ans += 1
			flag = flag ^ 1
		}
	}

	return ans + (len(nums)-ans)&1
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: {1,1,2,3,5}
 *TestCase 1: {1,1,2,2,3,3}
 *--TESTCASE END--
 */
func main() {
	fmt.Print(minDeletion([]int{1, 1, 2, 2, 3, 3}))
}

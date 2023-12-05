/* INTRODUCTION
 *日期: 2023-11-16
 *题目: K 个元素的最大和
 *链接: https://leetcode-cn.com/problems/maximum-sum-with-exactly-k-elements/
 */

package main

import "fmt"

// --CODE BEGIN--
func maximizeSum(nums []int, k int) int {
	maxNum := 0
	for _, num := range nums {
		if num > maxNum {
			maxNum = num
		}
	}
	return (2*maxNum + k - 1) * k / 2
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: [1,2,3,4,5],3
 *TestCase 1: [5,5,5],2
 *--TESTCASE END--
 */
func main() {
	fmt.Print(maximizeSum([]int{1, 2, 3, 4, 5}, 3))
}

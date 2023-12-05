/* INTRODUCTION
 *日期: 2023-11-16
 *题目: 最长奇偶子数组
 *链接: https://leetcode-cn.com/problems/longest-even-odd-subarray-with-threshold/
 */

package main

import (
	"fmt"
	"testing"
)

// --CODE BEGIN--
func longestAlternatingSubarray(nums []int, threshold int) int {
	n := len(nums)
	ans := 0
	i := 0
	for i < n {
		if nums[i]&1 == 0 && nums[i] <= threshold {
			start := i
			i += 1
			for i < n && nums[i] <= threshold && nums[i]&1 != nums[i-1]&1 {
				i += 1
			}
			ans = max(ans, i-start)
		} else {
			i += 1
		}
	}
	return ans
}

func max(a int, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: [3,2,5,4],5
 *TestCase 1: [1,2],2
 *TestCase 2: [2,3,4,5],4
 *--TESTCASE END--
 */
func TestSolution(t *testing.T) {
	if ans := longestAlternatingSubarray([]int{3, 2, 5, 4}, 5); ans != 3 {
		t.Errorf("Error output %d\n", ans)
	}
}

func main() {
	fmt.Print(longestAlternatingSubarray([]int{4, 10, 3}, 10))
}

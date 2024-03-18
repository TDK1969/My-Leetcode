/* INTRODUCTION
 * 日期: 2024-03-13
 * 题目: 字符串相加
 * 链接: https://leetcode.cn/problems/add-strings/
 */

package main

import (
	"fmt"
)

//--CODE BEGIN--

//lint:ignore U1000 Ignore unused function check
func addStrings(num1 string, num2 string) string {
	n1, n2 := len(num1), len(num2)
	t1, t2 := []byte(num1), []byte(num2)
	for i, j := 0, len(t1)-1; i < j; i, j = i+1, j-1 {
		t1[i], t1[j] = t1[j], t1[i]
	}
	for i, j := 0, len(t2)-1; i < j; i, j = i+1, j-1 {
		t2[i], t2[j] = t2[j], t2[i]
	}

	ans := make([]byte, 0)
	n := 0
	if n1 > n2 {
		n = n2
	} else {
		n = n1
	}
	var step byte = 0

	for i := 0; i < n; i++ {
		temp := t1[i] - 48 + t2[i] - 48 + step
		if temp >= 10 {
			step = 1
			temp = temp % 10
		} else {
			step = 0
		}
		ans = append(ans, temp+48)
	}

	for i := n; i < n1; i++ {
		temp := t1[i] - 48 + step
		if temp >= 10 {
			step = 1
			temp = temp % 10
		} else {
			step = 0
		}
		ans = append(ans, temp+48)
	}

	for i := n; i < n2; i++ {
		temp := t2[i] - 48 + step
		if temp >= 10 {
			step = 1
			temp = temp % 10
		} else {
			step = 0
		}
		ans = append(ans, temp+48)
	}
	if step != 0 {
		ans = append(ans, 49)
	}

	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}

	return string(ans)

}

func reverse(s string) []byte {
	res := make([]byte, 0)
	for i := len(s) - 1; i >= 0; i-- {
		res = append(res, s[i])
	}
	return res
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: "11","123"
 *TestCase 1: "456","77"
 *TestCase 2: "0","0"
 *--TESTCASE END--
 */
func main() {
	fmt.Print(addStrings("3876620623801494171", "6529364523802684779"))
}

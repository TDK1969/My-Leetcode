/*
 * @Descripttion:
 * @version:
 * @Author: TDK
 * @Date: 2023-11-16 19:53:43
 * @LastEditors: TDK
 * @LastEditTime: 2023-11-16 20:02:07
 */
/* INTRODUCTION
 *日期: 2023-11-16
 *题目: 二叉树的层平均值
 *链接: https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
 */

package main

//--CODE BEGIN--

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	var dfs func(root *TreeNode, layer int)
	maxLayer := 0
	type layerCount struct {
		sum int
		cnt int
	}
	layerMap := make(map[int]*layerCount)
	dfs = func(root *TreeNode, layer int) {
		maxLayer = max(maxLayer, layer)
		if layerMap[layer] == nil {
			layerMap[layer] = &layerCount{sum: 0, cnt: 0}
		}
		layerMap[layer].cnt += 1
		layerMap[layer].sum += root.Val

		if root.Left != nil {
			dfs(root.Left, layer+1)
		}
		if root.Right != nil {
			dfs(root.Right, layer+1)
		}
	}
	dfs(root, 1)
	ans := []float64{}

	for i := 1; i <= maxLayer; i++ {
		ans = append(ans, float64(layerMap[i].sum)/float64(layerMap[i].cnt))
	}
	return ans
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

//--CODE END--
/*--TESTCASE BEGIN--
 *TestCase 0: {3,9,20,nil,nil,15,7}
 *TestCase 1: {3,9,20,15,7}
 *--TESTCASE END--
 */
func main() {

}

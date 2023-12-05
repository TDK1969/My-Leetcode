/*
 * @Descripttion:
 * @version:
 * @Author: TDK
 * @Date: 2023-11-16 16:56:10
 * @LastEditors: TDK
 * @LastEditTime: 2023-11-16 19:24:31
 */
/* INTRODUCTION
 *日期: 2023-11-16
 *题目: 二叉树的右视图
 *链接: https://leetcode-cn.com/problems/binary-tree-right-side-view/
 */

package main

import "container/list"

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

//lint:ignore U1000 Ignore unused function check
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	type myNode struct {
		treeNode *TreeNode
		depth    int
	}
	var depth2RightVal = make(map[int]int)
	q := list.New()
	q.PushBack(&myNode{treeNode: root, depth: 0})
	maxDepth := -1

	for q.Len() != 0 {
		t := q.Front()
		q.Remove(t)
		node := t.Value.(*myNode)
		depth2RightVal[node.depth] = node.treeNode.Val
		maxDepth = max(maxDepth, node.depth)
		if node.treeNode.Left != nil {
			q.PushBack(&myNode{treeNode: node.treeNode.Left, depth: node.depth + 1})
		}
		if node.treeNode.Right != nil {
			q.PushBack(&myNode{treeNode: node.treeNode.Right, depth: node.depth + 1})
		}
	}
	ans := []int{}
	for i := 0; i <= maxDepth; i++ {
		ans = append(ans, depth2RightVal[i])
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
 *TestCase 0: {1,2,3,nil,5,nil,4}
 *TestCase 1: {1,nil,3}
 *TestCase 2: {}
 *--TESTCASE END--
 */
func main() {

}

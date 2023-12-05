/* INTRODUCTION
 *日期: 2023-11-16
 *题目: 二叉树的锯齿形层序遍历
 *链接: https://leetcode-cn.com/problems/binary-tree-zig zag-level-order-traversal/
 */

package main

import "container/list"

// --CODE BEGIN--
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//lint:ignore U1000 Ignore unused function check
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	ans := [][]int{}
	if root == nil {
		return ans
	}
	type myNode struct {
		tn    *TreeNode
		depth int
	}
	nxtQueue := list.New()
	nxtQueue.PushBack(&myNode{tn: root, depth: 0})

	for nxtQueue.Len() != 0 {
		curQueue := nxtQueue
		nxtQueue = list.New()
		for curQueue.Len() != 0 {
			temp := curQueue.Back()
			curQueue.Remove(temp)
			tempNode := temp.Value.(*myNode)
			if tempNode.depth == len(ans) {
				ans = append(ans, []int{})
			}
			ans[tempNode.depth] = append(ans[tempNode.depth], tempNode.tn.Val)
			if tempNode.depth&1 == 0 {
				if tempNode.tn.Left != nil {
					nxtQueue.PushBack(&myNode{tn: tempNode.tn.Left, depth: tempNode.depth + 1})
				}
				if tempNode.tn.Right != nil {
					nxtQueue.PushBack(&myNode{tn: tempNode.tn.Right, depth: tempNode.depth + 1})
				}
			} else {
				if tempNode.tn.Right != nil {
					nxtQueue.PushBack(&myNode{tn: tempNode.tn.Right, depth: tempNode.depth + 1})
				}
				if tempNode.tn.Left != nil {
					nxtQueue.PushBack(&myNode{tn: tempNode.tn.Left, depth: tempNode.depth + 1})
				}
			}
		}

	}

	return ans
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: {3,9,20,nil,nil,15,7}
 *TestCase 1: {1}
 *TestCase 2: {}
 *--TESTCASE END--
 */
func main() {

}

/* INTRODUCTION
 *日期: 2023-11-16
 *题目: 二叉树的最近公共祖先
 *链接: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
 */

package main

import (
	"testing"
)

//--CODE BEGIN--
/*
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

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root == p || root == q {
		return root
	}
	l, r := lowestCommonAncestor(root.Left, p, q), lowestCommonAncestor(root.Right, p, q)
	if l != nil && r != nil {
		return root
	} else if l != nil {
		return l
	} else {
		return r
	}
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: [3,5,1,6,2,0,8,nil,nil,7,4],5,1
 *TestCase 1: [3,5,1,6,2,0,8,nil,nil,7,4],5,4
 *TestCase 2: [1,2],1,2
 *--TESTCASE END--
 */
func TestSolution(t *testing.T) {

}

func main() {
	lowestCommonAncestor(nil, nil, nil)
}

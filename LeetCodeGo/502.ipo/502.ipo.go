/* INTRODUCTION
 *日期: 2024-03-19
 *题目: IPO
 *链接: https://leetcode.cn/problems/ipo/
 */

package main

import (
	"container/heap"
	"fmt"
)

//--CODE BEGIN--

//lint:ignore U1000 Ignore unused function check

type hp struct {
	profit int
	pq     [][]int
}

func (h hp) Len() int {
	return len(h.pq)
}

func (h hp) Less(i, j int) bool {
	t1, t2 := -1, -1
	if h.profit-h.pq[i][0] >= 0 {
		t1 = h.pq[i][1]
	}
	if h.profit-h.pq[j][0] >= 0 {
		t2 = h.pq[j][1]
	}
	return t1 > t2
}

func (h hp) Swap(i, j int) {
	h.pq[i], h.pq[j] = h.pq[j], h.pq[i]
}

func (h *hp) Pop() interface{} {
	old := h.pq
	n := len(old)
	x := h.pq[n-1]
	h.pq = old[0 : n-1]
	return x
}

func (h *hp) Push(x interface{}) {
	h.pq = append(h.pq, x.([]int))
}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	h := &hp{profit: w}
	for i := range profits {
		h.pq = append(h.pq, []int{capital[i], profits[i]})
	}
	heap.Init(h)
	for ; k > 0 && h.Len() > 0; k-- {
		t := heap.Pop(h).([]int)
		if t[0] > h.profit {
			break
		}
		h.profit += t[1]
	}
	return h.profit
}

//--CODE END--

/*--TESTCASE BEGIN--
 *TestCase 0: 2,0,{1,2,3},{0,1,1}
 *TestCase 1: 3,0,{1,2,3},{0,1,2}
 *--TESTCASE END--
 */
func main() {
	fmt.Print(findMaximizedCapital(3, 0, []int{1, 2, 3}, []int{0, 1, 2}))
}

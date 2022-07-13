/*
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
*/
//递减栈，当前元素小于栈顶元素直接入栈；大于栈顶元素则出栈栈顶元素再入栈 
#include <stdlib.h>
typedef struct  {
    int temperature;
    int order;
} daily_temp;

int* dailyTemperatures(int* T, int TSize, int* returnSize)
{
    int *higher = (int *)malloc(sizeof(int) * TSize);
    daily_temp stack[30005];
    int top = -1;
    *returnSize = TSize;
    int i = 0;
    while (i < TSize) {
        if (top == -1 || stack[top].temperature >= T[i]) {//入栈
            top++;
            stack[top].temperature = T[i];
            stack[top].order = i;
        } else if (stack[top].temperature < T[i]) {//出栈
            higher[stack[top].order] = i - stack[top].order;
            top--;
            continue;
        }
        i++;
    }

    while (top != -1) {//剩下的都是后面没有更大的
        higher[stack[top].order] = 0;
        top--;
    }

    return higher;
}
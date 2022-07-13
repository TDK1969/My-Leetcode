/*
�����ÿ�� ���� �б���������һ���б���Ӧλ�õ����Ϊ��Ҫ��۲⵽���ߵ����£�������Ҫ�ȴ���������
�����������֮�󶼲������ߣ����ڸ�λ���� 0 �����档

���磬����һ���б� temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
������Ӧ���� [1, 1, 4, 2, 1, 1, 0, 0]��

��ʾ������ �б��ȵķ�Χ�� [1, 30000]��ÿ�����µ�ֵ�ľ�Ϊ���϶ȣ������� [30, 100] ��Χ�ڵ�������
*/
//�ݼ�ջ����ǰԪ��С��ջ��Ԫ��ֱ����ջ������ջ��Ԫ�����ջջ��Ԫ������ջ 
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
        if (top == -1 || stack[top].temperature >= T[i]) {//��ջ
            top++;
            stack[top].temperature = T[i];
            stack[top].order = i;
        } else if (stack[top].temperature < T[i]) {//��ջ
            higher[stack[top].order] = i - stack[top].order;
            top--;
            continue;
        }
        i++;
    }

    while (top != -1) {//ʣ�µĶ��Ǻ���û�и����
        higher[stack[top].order] = 0;
        top--;
    }

    return higher;
}
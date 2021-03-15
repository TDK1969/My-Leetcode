
#include <stdbool.h>
#include <stdlib.h>
typedef struct {
    int Queue1[10005];
    int head1, rear1;
    int Queue2[10005];
    int head2, rear2;
} MyStack;

/** Initialize your data structure here. */

MyStack* myStackCreate() {
    MyStack * stack = (MyStack *)malloc(sizeof(MyStack));
    stack->head1 = stack->head2 = stack->rear1 = stack->rear2 = -1;
    return stack;
}

/** Push element x onto stack. */
void myStackPush(MyStack* obj, int x) {
    if (obj->head1 == -1) {
        obj->head1++;
        obj->Queue1[++obj->rear1] = x;
    } else {
        obj->Queue1[++obj->rear1] = x;
    }
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack* obj) {
    while (obj->head1 != obj->rear1) {
        if (obj->head2 == -1) {
            obj->head2++;
        }

        obj->Queue2[++obj->rear2] = obj->Queue1[obj->head1++];
    }

    int ans = obj->Queue1[obj->head1];
    obj->head1 = obj->rear1 = -1;

    while (obj->head2 != -1 && obj->head2 <= obj->rear2) {
        if (obj->head1 == -1) {
            obj->head1++;
        }

        obj->Queue1[++obj->rear1] = obj->Queue2[obj->head2++];
    }
    obj->head2 = obj->rear2 = -1;
    return ans;
}

/** Get the top element. */
int myStackTop(MyStack* obj) {
    int RearElem = myStackPop(obj);
    myStackPush(obj, RearElem);
    return RearElem;
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack* obj) {
    return (obj->head1 == -1);
}

void myStackFree(MyStack* obj) {
    free(obj);
}    
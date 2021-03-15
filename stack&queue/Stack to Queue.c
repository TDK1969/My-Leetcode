#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int in_stack[10005];
    int in_top;
    int out_stack[10005];
    int out_top;
} MyQueue;

/** Initialize your data structure here. */

MyQueue* myQueueCreate() {
    MyQueue * queue = (MyQueue *)malloc(sizeof(MyQueue));
    queue->in_top = -1;
    queue->out_top = -1;
    return queue;
}

/** Push element x to the back of queue. */
void myQueuePush(MyQueue* obj, int x) {
    obj->in_top++;
    obj->in_stack[obj->in_top] = x;
}

/** Removes the element from in front of queue and returns that element. */
int myQueuePop(MyQueue* obj) {
    if (obj->out_top == -1) {
        while (obj->in_top != -1) {
            obj->out_stack[++obj->out_top] = obj->in_stack[obj->in_top--];
        }
    }

    return obj->out_stack[obj->out_top--];
}

/** Get the front element. */
int myQueuePeek(MyQueue* obj) {
    if (obj->out_top == -1) {
        while (obj->in_top != -1) {
            obj->out_stack[++obj->out_top] = obj->in_stack[obj->in_top--];
        }
    }

    return obj->out_stack[obj->out_top];
}

/** Returns whether the queue is empty. */
bool myQueueEmpty(MyQueue* obj) {
    return (obj->in_top == -1 && obj->out_top == -1);
}

void myQueueFree(MyQueue* obj) {
    free(obj);
}

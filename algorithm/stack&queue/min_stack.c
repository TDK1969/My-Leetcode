 typedef struct {
    int mainstack[10000];
    int minstack[10000];
    int maintop;
    int mintop;
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
    MinStack *stack = (MinStack *)malloc(sizeof(MinStack));
    stack->maintop = -1;
    stack->mintop = -1;
    return stack;
}

void minStackPush(MinStack* obj, int x) {
    obj->mainstack[++obj->maintop] = x;
    if (obj->mintop == -1) {
        obj->minstack[++obj->mintop] = x;
    } else if (x <= obj->minstack[obj->mintop]) {
        obj->minstack[++obj->mintop] = x;
    }
}

void minStackPop(MinStack* obj) {
    int temp = obj->mainstack[obj->maintop--];
    if (temp == obj->minstack[obj->mintop]) {
        obj->mintop--;
    }
}

int minStackTop(MinStack* obj) {
    return obj->mainstack[obj->maintop];
}

int minStackGetMin(MinStack* obj) {
    return obj->minstack[obj->mintop];
}

void minStackFree(MinStack* obj) {
    free(obj);
}
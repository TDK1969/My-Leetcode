#include <stdlib.h>

struct Node {
    int val;
    int numNeighbors;
    struct Node** neighbors;
 };
 

    struct Node *cloneGraph(struct Node *s) {
        struct Node *copy = (struct Node *)malloc(sizeof(struct Node) * 105);
        for (int i = 0; i < 105; i++) {
            copy[i].neighbors = (struct Node **)malloc(sizeof(struct Node *) * 100);
            copy[i].numNeighbors = 0;
            copy[i].val = i;
        }

        struct Node *root = &copy[s->val];//to return
        struct Node *stack[105];
        int top = -1;

        stack[++top] = s;

        while (top != -1) {
            struct Node *temp = stack[top--];
            struct Node *copytemp = &copy[temp->val];
            copytemp->numNeighbors = temp->numNeighbors;
            for (int i = 0; i < temp->numNeighbors; i++) {
                if (copy[temp->neighbors[i]->val].numNeighbors != 0) {//未访问的节点numneighbor为0
                    continue;
                }
                stack[++top] = temp->neighbors[i];
                copytemp->neighbors[i] = &copy[temp->neighbors[i]->val];
            }
        }
        return root;
        
    }
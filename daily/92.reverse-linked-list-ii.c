#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <ctype.h>
#include <math.h>
#include <signal.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
typedef struct ListNode ListNode;
ListNode* stack[500];
int top = -1;
struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    ListNode* start = head;
    ListNode* pre = NULL;
    for (int i = 1; i < left; i++) {
        pre = start;
        start = start->next;
    }
    
    for (int i = left; i <= right; i++) {
        stack[++top] = start;
        start = start->next;
    }
    ListNode* temp;
    for (int i = left; i <= right; i++) {
        temp = stack[top--];
        if (pre == NULL) {
            head = temp;
        } else {
            pre->next = temp;
        }
        pre = temp;
    }

    temp->next = start;
    return head;


}

int main()
{
    return 0;
}
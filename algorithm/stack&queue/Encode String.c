#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char * decodeString(char * s){
    int stack[100005];
    int top = -1;
    char *ans_string = (char *)malloc(sizeof(char) * 100000000);
    
    int i = 0;
    int j = 0;
    int next;
    int len = strlen(s);
    stack[++top] = i;

    while (top != -1) {
        int temp = stack[top--];
        if (temp == -1) {
            temp = next;
        }
        
        if (temp >= len) {
            continue;
        }
        
        if (s[temp] == ']') {
            next = temp + 1;
            continue;
        } else if (s[temp] >= 'a' && s[temp] <= 'z' || s[temp] >= 'A' && s[temp] <= 'Z') {
            ans_string[j++] = s[temp];
            stack[++top] = temp + 1;
        } else {
            int times = atoi(s + temp);
            stack[++top] = -1;
            while (s[temp] != '[') {
                temp++;
            }
            while (times--) {
                stack[++top] = temp + 1;
            }
        }
    }
    ans_string[j] = '\0';
    return ans_string;
}

int main()
{
    char name[20] = "100[leetcode]";
    char *ans = decodeString(name);
    printf("%s", ans);
    return 0;
}


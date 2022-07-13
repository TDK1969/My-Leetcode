#include <stdbool.h>

bool isValid(char * s)
{
    char stack[100000];
    int top = -1;
    int i = 0;
    char temp = s[i];
    while (temp != '\0') {
        switch(temp) {
            case '(':
            case '[':
            case '{':
                stack[++top] = temp;
                break;
            case ')':
                if (top == -1 || stack[top--] != '(') {
                    return false;
                }
                break;
            case ']':
                if (top == -1 || stack[top--] != '[') {
                    return false;
                }
                break;
            case '}':
                if (top == -1 || stack[top--] != '{') {
                    return false;
                }
                break;
        }
        temp = s[++i];
    }
    if (top != -1) {
        return false;
    }
    return true;
}
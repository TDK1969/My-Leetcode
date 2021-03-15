
#include <stdlib.h>
int evalRPN(char ** tokens, int tokensSize){
    int stack[10005];
    int top = -1;

    int i = 0;

    while (i < tokensSize) {
        char *str = tokens[i];
        if ((str[0] == '+' || str[0] == '-' || str[0] == '*' || str[0] == '/') && str[1] == '\0') {
            int num2 = stack[top--];
            int num1 = stack[top--];
            int res;
            switch(str[0]) {
                case '+' :
                    res = num1 + num2;
                    break;
                case '-' :
                    res = num1 - num2;
                    break;
                case '*' :
                    res = num1 * num2;
                    break;
                case '/' :
                    res = num1 / num2;
                    break;
            }
            stack[++top] = res;
        } else {
            int num = atoi(str);
            stack[++top] = num;
        }
        i++;
    }
    return stack[top];
}
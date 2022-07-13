#include <stdbool.h>

bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize){
    int stack[3050];
    int top = -1;

    int *visited = (int *)malloc(sizeof(int) * roomsSize);
    for (int i = 0; i < roomsSize; i++) {
        visited[i] = 0;
    }

    stack[++top] = 0;
    visited[0] = 1;

    while (top != -1) {
        int temp = stack[top--];

        for (int i = 0; i < roomsColSize[temp]; i++) {
            int nextroom = rooms[temp][i];
            if (visited[nextroom] == 0) {
                visited[nextroom] = 1;
                stack[++top] = nextroom;
            }
        }
    }

    for (int i = 0; i < roomsSize; i++) {
        if (visited[i] == 0) {
            return false;
        }
    }
    return true;
}
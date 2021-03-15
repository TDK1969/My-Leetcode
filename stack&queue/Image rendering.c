#include <stdlib.h>
#include <stdio.h>

int visited[50][50];
int dir[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
typedef struct {
    int x;
    int y;
} point;

int** floodFill(int** image, int imageSize, int* imageColSize,\
 int sr, int sc, int newColor, \
 int* returnSize, int** returnColumnSizes)
{
    *returnSize = imageSize;
    int **NewImage = (int **)malloc(sizeof(int *) * imageSize);
    *returnColumnSizes = (int *)malloc(sizeof(int) * imageSize);

    for (int i = 0; i < imageSize; i++) {
        *returnColumnSizes[i] = imageColSize[i];
        NewImage[i] = (int *)malloc(sizeof(int) * imageColSize[i]);
        for (int j = 0; j < imageColSize[i]; j++) {
            NewImage[i][j] = image[i][j];
        }
    }

    point stack[2550];
    int top = -1;

    top++;
    stack[top].x = sr;
    stack[top].y = sc;
    visited[sr][sc] = 1;
    int origin = image[sr][sc];
    while (top != -1) {
        point temp = stack[top--];
        if (image[temp.x][temp.y] == origin) {
            NewImage[temp.x][temp.y] = newColor;
        }

        for (int i = 0; i < 4; i++) {
            int nextx = temp.x + dir[i][0];
            int nexty = temp.y + dir[i][1];
            if (nextx >= 0 && nextx < imageSize && nexty >=0 && nexty < imageColSize[i] && visited[nextx][nexty] == 0) {
                top++;
                stack[top].x = nextx;
                stack[top].y = nexty;
                visited[nextx][nexty] = 1;
            }
        }
    }
    return NewImage;
}
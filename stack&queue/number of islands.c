void _numIslands(char** grid, int rowSize, int colSize, int i, int j){
    if(i < 0 || i >= rowSize || j < 0 || j >= colSize){
        return ;
    }
    
    if(grid[i][j] == '1'){
        grid[i][j] = '2';
        _numIslands(grid, rowSize, colSize, i-1, j);
        _numIslands(grid, rowSize, colSize, i+1, j);
        _numIslands(grid, rowSize, colSize, i, j-1);
        _numIslands(grid, rowSize, colSize, i, j+1);
    }
}

int numIslands(char** grid, int gridSize, int* gridColSize){
    int cnt = 0;
    for(int i = 0; i < gridSize; i++){
        for(int j = 0; j < gridColSize[0]; j++){
            if(grid[i][j] == '1'){
                cnt++;
                _numIslands(grid, gridSize, gridColSize[0], i, j);
            }
        }
    }
    
    return cnt;
}
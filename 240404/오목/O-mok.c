#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define BOARD_SIZE 19

static int dd[5] = {-2,-1,0,1,2};

int main() {
    int board[BOARD_SIZE][BOARD_SIZE];
    int target, count, row, col, res = 0, nr, nc;
    bool find = false;

    for(int i = 0; i < BOARD_SIZE; i++)
        for(int j = 0; j < BOARD_SIZE; j++)
            scanf("%d", &board[i][j]);
    
    for(int r = 0; r < BOARD_SIZE; r++) {
        for(int c = 0; c < BOARD_SIZE; c++) {
            if(board[r][c] != 0) {
                target = board[r][c];
                // vertical line
                count = 0;
                for(int i = 0; i < 5; i++) {
                    nr = r + dd[i];
                    nc = c;
                    if(nr >= 0 && nr < BOARD_SIZE)
                        if(board[nr][nc] == target)
                            count++;
                }
                if(count == 5) {
                    row = r+1;
                    col = c+1;
                    res = target;
                    find = true;
                    break;
                }
                // diagonal line NE
                count = 0;
                for(int i = 0; i < 5; i++) {
                    nr = r + dd[i];
                    nc = c - dd[i];
                    if(nr >= 0 && nr < BOARD_SIZE && nc >= 0 && nc < BOARD_SIZE)
                        if(board[nr][nc] == target)
                            count++;
                }
                if(count == 5) {
                    row = r+1;
                    col = c+1;
                    res = target;
                    find = true;
                    break;
                }
                // horizontal line
                count = 0;
                for(int i = 0; i < 5; i++) {
                    nr = r;
                    nc = c + dd[i];
                    if(nc >= 0 && nc < BOARD_SIZE)
                        if(board[nr][nc] == target)
                            count++;
                }
                if(count == 5) {
                    row = r+1;
                    col = c+1;
                    res = target;
                    find = true;
                    break;
                }
                // diagonal line NW
                count = 0;
                for(int i = 0; i < 5; i++) {
                    nr = r + dd[i];
                    nc = c + dd[i];
                    if(nr >= 0 && nr < BOARD_SIZE && nc >= 0 && nc < BOARD_SIZE)
                        if(board[nr][nc] == target)
                            count++;
                }
                if(count == 5) {
                    row = r+1;
                    col = c+1;
                    res = target;
                    find = true;
                    break;
                }
            }
        }
        if(find) break;
    }

    if(res)
        printf("%d\n%d %d\n",res,row,col);
    else
        printf("%d\n",res);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int dr[8] = {-1,-1,0,1,1,1,0,-1};
static int dc[8] = {0,1,1,1,0,-1,-1,-1};

int main() {
    int N, M, count = 0, checker, nr, nc;
    char board[50][50];

    scanf("%d %d",&N,&M);

    for(int i = 0; i < N; i++)
        scanf("%s",&board[i]);

    for(int row = 0; row < N; row++) {
        for(int col = 0; col < M; col++) {
            if(board[row][col] == 'L') {
                for(int d = 0; d < 8; d++) {
                    checker = 0;
                    nr = row + dr[d];
                    nc = col + dc[d];
                    if(nr >= 0 && nr < N && nc >= 0 && nc < M)
                        if(board[nr][nc] == 'E') checker++;
                    nr += dr[d];
                    nc += dc[d];
                    if(nr >= 0 && nr < N && nc >= 0 && nc < M)
                        if(board[nr][nc] == 'E') checker++;
                    if(checker == 2) count++;
                }
            }
        }
    }

    printf("%d\n",count);
    return 0;
}
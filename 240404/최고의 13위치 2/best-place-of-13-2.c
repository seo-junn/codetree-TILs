#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, board[20][20], count1, count2, max_count = 0;

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            scanf("%d", &board[i][j]);
    
    for(int row = 0; row < N; row++)
        for(int col = 0; col < N-2; col++) {
            count1 = board[row][col]+board[row][col+1]+board[row][col+2];
            for(int r = row; r < N; r++) {
                if(r == row) {
                    for(int c = col+3; c < N-2; c++) {
                        count2 = board[r][c]+board[r][c+1]+board[r][c+2];
                        if(max_count < count1+count2)
                            max_count = count1 + count2;
                    }
                } else {
                    for(int c = 0; c < N-2; c++) {
                        count2 = board[r][c]+board[r][c+1]+board[r][c+2];
                        if(max_count < count1+count2)
                            max_count = count1 + count2;
                    }
                }
            }
        }

    printf("%d\n",max_count);
    return 0;
}
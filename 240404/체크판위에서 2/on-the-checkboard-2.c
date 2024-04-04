#include <stdio.h>
#include <stdlib.h>

int main() {
    int R, C, count = 0;
    char board[15][15],temp;

    scanf("%d %d",&R,&C);
    int r = 0, c = 0;
    while(r < R && c < C) {
        scanf("%c",&temp);
        if (temp != ' ' && temp != '\n') {
            board[r][c] = temp;
            c++;
            if(c == C) {
                c = 0;
                r++;
            }
        }
    }
    
    if (board[0][0] == board[R-1][C-1])
        count = 0;
    else {
        count = 0;
        for(int row = 1; row < R; row++)
            for(int col = 1; col < C; col++)
                if (board[row][col] != board[0][0])
                    for(int r = row+1; r < R-1; r++)
                        for(int c = col+1; c < C-1; c++)
                            if (board[r][c] == board[0][0])
                                count++;
    }

    printf("%d\n",count);

    return 0;
}
#include <stdio.h>

int main() {
    int N, board[20][20], max_cnt = 0, temp;

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            scanf("%d",&board[i][j]);
    
    for(int row = 0; row < N; row++) {
        for(int col = 0; col < N-2; col++) {
            temp = 0;
            for(int i = 0; i < 3; i++)
                temp += board[row][col+i];
            if(temp > max_cnt)
                max_cnt = temp;
        }
    }

    printf("%d\n",max_cnt);

    return 0;
}
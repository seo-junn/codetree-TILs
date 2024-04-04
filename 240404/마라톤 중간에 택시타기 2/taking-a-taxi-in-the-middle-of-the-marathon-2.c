#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int N, pos[100][2], base = 0, temp, ans = INT_MAX;

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        scanf("%d %d",&pos[i][0],&pos[i][1]);

    for(int i = 1; i < N; i++)
        base += abs(pos[i][0]-pos[i-1][0]) + abs(pos[i][1]-pos[i-1][1]);
    
    for(int i = 1; i < N-1; i++) {
        temp = abs(pos[i][0]-pos[i-1][0]) + abs(pos[i][1]-pos[i-1][1]) + abs(pos[i][0]-pos[i+1][0]) + abs(pos[i][1]-pos[i+1][1]) - abs(pos[i-1][0]-pos[i+1][0]) - abs(pos[i-1][1]-pos[i+1][1]);
        temp = base-temp;
        if (ans > temp)
            ans = temp;
    }

    printf("%d\n",ans);

    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int N, rooms[1003], ans = INT_MAX, dist, idx, count, temp;

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        scanf("%d",&rooms[i]);

    for(int target = 0; target < N; target++) {
        idx = target;
        count = 0;
        dist = 0;
        temp = 0;
        while(count < N) {
            temp += rooms[idx]*dist;
            idx = (idx+1)%N;
            count++;
            dist++;
        }
        if(ans > temp)
            ans = temp;
    }

    printf("%d\n",ans);
    return 0;
}
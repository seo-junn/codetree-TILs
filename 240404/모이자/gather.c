#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int N, ans = INT_MAX, temp;
    int nums[100];

    scanf("%d",&N);
    for(int i = 0; i < N; i++) {
        scanf("%d",&nums[i]);
    }
    
    for(int target = 0; target < N; target++) {
        temp = 0;
        for(int i = 0; i < N; i++) {
            if (target == i) continue;
            temp += abs(target-i)*nums[i];
        }
        if(temp < ans)
            ans = temp;
    }

    printf("%d\n",ans);
    return 0;
}
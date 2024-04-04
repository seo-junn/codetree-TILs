#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int N, S, nums[100], base = 0, temp, diff, ans = INT_MAX;

    scanf("%d %d",&N,&S);
    for(int i = 0; i < N; i++) {
        scanf("%d",&nums[i]);
        base += nums[i];
    }
    
    for(int i = 0; i < N; i++)
        for(int j = i+1; j < N; j++) {
            temp = base - nums[i] - nums[j];
            diff = abs(S-temp);
            if(diff < ans)
                ans = diff;
        }
    
    printf("%d\n", ans);

    return 0;
}
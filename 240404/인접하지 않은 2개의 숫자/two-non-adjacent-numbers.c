#include <stdio.h>

int main() {
    int N, nums[100], ans = 0, temp;

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        scanf("%d",&nums[i]);
    
    for(int i = 0; i < N; i++)
        for(int j = i+2; j < N; j++) {
            temp = nums[i] + nums[j];
            if (ans < temp)
                ans = temp;
        }
    
    printf("%d\n",ans);
    return 0;
}
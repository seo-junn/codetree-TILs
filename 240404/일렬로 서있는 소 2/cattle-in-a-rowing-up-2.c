#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, count = 0, cows[100];

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        scanf("%d",&cows[i]);
    
    for(int i = 0; i < N; i++) {
        for(int j = i+1; j < N; j++) {
            if(cows[i] <= cows[j]) {
                for(int k = j+1; k < N; k++) {
                    if(cows[j] <= cows[k]) {
                        count++;
                    }
                }
            }
        }
    }

    printf("%d\n",count);

    return 0;
}
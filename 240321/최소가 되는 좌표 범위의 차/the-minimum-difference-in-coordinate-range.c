#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define min(x, y) (x) < (y) ? (x) : (y)

int dot_comp(const void* d1, const void* d2){
    int *a, *b;
    a = (int*)d1;
    b = (int*)d2;
    if (a[1] < b[1]) return -1;
    else return 1;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int N, D;
    scanf("%d %d",&N,&D);
    int dots[N][2];

    for(int i = 0; i < N; i++) {
        scanf("%d %d",&dots[i][0],&dots[i][1]);
    }

    qsort(dots,N,sizeof(dots[0]),dot_comp);

    int dist = 10000000;
    int left, right;

    for(left = 0; left < N; left++) {
        right = N-1;
        while(left < right) {
            if (dots[right][1]-dots[left][1] >= D) {
                dist = min(dist,abs(dots[left][0]-dots[right][0]));
                right--;
            }
            else break;
        }
    }

    printf("%d\n",dist);

    return 0;
}
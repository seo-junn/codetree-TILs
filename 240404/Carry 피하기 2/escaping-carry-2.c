#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    int N, nums[20], A, B, C, ans = -1, temp;
    bool carry;

    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        scanf("%d",&nums[i]);
    
    for(int i = 0; i < N; i++) {
        for(int j = i+1; j < N; j++) {
            for(int k = j+1; k < N; k++) {
                A = nums[i];
                B = nums[j];
                C = nums[k];
                carry = true;
                while (A > 0 || B > 0 || C > 0) {
                    if (A % 10 + B % 10 + C % 10 >= 10) {
                        carry = false;
                        break;
                    }
                    A /= 10;
                    B /= 10;
                    C /= 10;
                }
                if (carry) {
                    temp = nums[i]+nums[j]+nums[k];
                    if (ans < temp)
                        ans = temp;
                }
            }
        }
    }

    printf("%d\n", ans);
    return 0;
}
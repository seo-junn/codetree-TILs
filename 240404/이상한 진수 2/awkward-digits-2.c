#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char number[11];
    int target = -1, ans = 0, base;

    scanf("%s",number);
    for(int i = 0; i < strlen(number); i++) {
        if(number[i] == '0') {
            target = i;
            break;
        }
    }
    if(target == -1){
        for(int i = strlen(number)-1; i >= 0; i--) {
            if(number[i] == '1'){
                target = i;
                break;
            }
        }
        number[target] = '0';
        
    } else {
        number[target] = '1';
    }
    base = 1;
    for(int i = strlen(number)-1; i >= 0; i--) {
        ans += base*(number[i]-48);
        base *= 2;
    }
    printf("%d\n",ans);
    return 0;
}
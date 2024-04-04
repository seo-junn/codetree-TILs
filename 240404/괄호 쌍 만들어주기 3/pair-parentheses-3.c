#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char line[101];
    int count = 0;

    scanf("%s",line);
    for(int i = 0; i < strlen(line); i++){
        if (line[i] == '(') {
            for(int j = i+1; j < strlen(line);j++) {
                if (line[j] == ')') {
                    count += 1;
                }
            }
        }
    }

    printf("%d\n",count);
    return 0;
}
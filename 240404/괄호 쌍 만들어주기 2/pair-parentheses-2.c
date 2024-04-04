#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char line[101];
    int length, count = 0;

    scanf("%s",line);
    length = strlen(line);

    for(int l = 0; l < length-1; l++)
        if (line[l] == '(' && line[l+1] == '(')
            for(int r = l + 2; r < length-1; r++)
                if (line[r] == ')' && line[r+1] == ')')
                    count++;

    printf("%d\n",count);
    return 0;
}
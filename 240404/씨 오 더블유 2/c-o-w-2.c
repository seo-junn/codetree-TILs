#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int N, count = 0;
    char line[101];

    scanf("%d",&N);
    scanf("%s",line);
    
    for(int i = 0; i < N; i++)
        if (line[i] == 'C')
            for(int j = i+1; j < N; j++)
                if (line[j] == 'O')
                    for(int k = j+1; k < N; k++)
                        if (line[k] == 'W')
                            count++;

    printf("%d\n",count);
    return 0;
}
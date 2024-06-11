#include <iostream>

int check(int a, int b) {
    int count = 0;
    for(int i = a; i <= b; i++) {
        bool prime = true;
        for(int j = 2; j < i; j++) {
            if(i%j == 0) {
                prime = false;
                break;
            }
        }
        if(prime) {
            int temp = 0,now = i;
            while(now) {
                temp += now%10;
                now /= 10;
            }
            if(temp%2 == 0) count++;
        }
    }
    return count;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << check(a,b) << std::endl;

    return 0;
}
#include <iostream>

int main() {
    int a,b,cnt = 0;
    std::cin >> a >> b;
    for(int i = a; i <= b; i++) {
        if(i%3 == 0) cnt++;
        else {
            int temp = i;
            while(temp) {
                if(temp%10 == 3 || temp%10 == 6 || temp%10 == 9) {
                    cnt++;
                    break;
                }
                temp /= 10;
            }
        }
    }
    std::cout << cnt << "\n";
    return 0;
}
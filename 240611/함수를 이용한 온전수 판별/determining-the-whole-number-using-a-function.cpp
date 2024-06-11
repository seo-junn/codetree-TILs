#include <iostream>

int count(int a, int b) {
    int res = 0;
    for(int i = a; i <=b; i++) {
        if(i%2 == 0) continue;
        if(i%10 == 5) continue;
        if(i%3 == 0 && i%9 != 0) continue;
        res++;
    }
    return res;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << count(a,b) << std::endl;
    return 0;
}
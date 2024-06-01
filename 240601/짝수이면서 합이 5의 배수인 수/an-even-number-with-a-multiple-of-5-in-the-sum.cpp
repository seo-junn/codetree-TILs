#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if(n%2) std::cout << "No\n";
    else {
        int temp = 0;
        while(n) {
            temp += n%10;
            n /= 10;
        }
        if(temp%5) std::cout << "No\n";
        else std::cout << "Yes\n";
    }
    return 0;
}
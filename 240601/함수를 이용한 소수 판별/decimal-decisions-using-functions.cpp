#include <iostream>

bool is_prime(int n) {
    if(n == 1) return false
    for(int i = 2; i < n; i++) {
        if(n%i == 0) return false;
    }
    return true;
}

int main() {
    int a, b, res = 0;
    std::cin >> a >> b;
    for(int i = a; i <= b; i++)
        if(is_prime(i))
            res += i;
    std::cout << res << std::endl;
    return 0;
}
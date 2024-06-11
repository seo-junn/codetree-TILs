#include <iostream>

long long power(long long a, long long b) {
    long long ans = 1;
    for(int i = 0; i < b; i++)
        ans *= a;
    return ans;
}

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << power(a,b) << std::endl;
    return 0;
}
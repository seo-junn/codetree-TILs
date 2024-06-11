#include <iostream>

bool check(int M, int D) {
    int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if(M > 12) return false;
    if(D > month[M]) return false;
    return true;
}

int main() {
    int M, D;
    std::cin >> M >> D;
    std::cout << (check(M,D)?"Yes":"No") << std::endl;
    return 0;
}
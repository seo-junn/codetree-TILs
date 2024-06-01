#include <iostream>

bool moon_year(int y) {
    if(y%400 == 0) return true;
    else if(y%100 == 0) return false;
    else if(y%4 == 0) return true;
    else return false;
}

int main() {
    int y;
    std::cin >> y;
    std::cout << (moon_year(y)?"true":"false") << std::endl;
    return 0;
}
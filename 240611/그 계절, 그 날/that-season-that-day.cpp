#include <iostream>

bool leap_year(int Y);
int season(int Y, int M, int D);

int main() {
    int Y,M,D,res;
    char seasons[4][7] = {"Spring", "Summer", "Fall", "Winter"};
    std::cin >> Y >> M >> D;
    res = season(Y,M,D);
    if(res == -1) std::cout << res << std::endl;
    else std::cout << seasons[res] << std::endl;
    return 0;
}

bool leap_year(int Y) {
    if(Y%400 == 0) return true;
    else if(Y%100 == 0) return false;
    else if(Y%4 == 0) return true;
    else return false;
}

int season(int Y, int M, int D) {
    int month[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    if(leap_year(Y)) month[2]++;
    if(M > 12) return -1;
    if(D > month[M]) return -1;
    if(M>3 && M <6) return 0;
    if(M>5 && M <9) return 1;
    if(M>8 && M <12) return 2;
    return 3;
}
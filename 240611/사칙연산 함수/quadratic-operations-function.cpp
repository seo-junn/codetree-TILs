#include <iostream>

int cal(int a, char o, int c) {
    if(o == '+') return a+c;
    else if(o == '-') return a-c;
    else if(o == '/') return a/c;
    else if(o == '*') return a*c;
    else return -1;
}

int main() {
    int a, c, res;
    char o;

    std::cin >> a >> o >> c;
    res = cal(a,o,c);

    if(res == -1) std::cout << "False" << std::endl;
    else std::cout << a << " " << o <<" " << c << " = " << res << std::endl;
    
    return 0;
}
#include <iostream>

bool check(int n1, int n2, const int A[], const int B[]) {
    int count = 0;
    for(int i = 0; i < n1; i++) {
        if(A[i] == B[count]) count++;
        else count = 0;
        if(count == n2) return true;
    }
    return false;
}

int main() {
    int n1,n2;
    std::cin >> n1 >> n2;
    int A[n1], B[n2];
    for(int i = 0; i < n1; i++) std::cin >> A[i];
    for(int i = 0; i < n2; i++) std::cin >> B[i];
    std::cout << (check(n1,n2,A,B)?"Yes":"No") << std::endl;
    return 0;
}
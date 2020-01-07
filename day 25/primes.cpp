#include <iostream>
using namespace std;

string simpleCheck(int n){
    if (n == 2) return "Prime";
    else if (n < 2 || n%2==0) return "Not prime";
    for (int i = 3; i*i <= n; i+=2){
        if (n%i==0) return "Not prime";
    }
    return "Prime";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        int n;
        cin >> n;
        cout << simpleCheck(n) << endl;
    }
    return 0;
}

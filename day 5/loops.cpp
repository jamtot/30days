#include <bits/stdc++.h>

using namespace std;

void firstTen(int n){
    for (int i = 1; i < 11; i++)
    {
        cout << n << " x " << i << " = " << n*i << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    firstTen(n);
    return 0;
}

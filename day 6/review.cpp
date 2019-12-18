#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    string input;
    
    for (int i = 0; i < n; i++){
        cin >> input;
        string odd,even ="";
        for (int j = 0; j < input.length(); j++){
            if (j%2==1)
                odd+=input[j];
            else
                even+=input[j];
        }
        cout << even << " " << odd << endl;
    }

    return 0;
}

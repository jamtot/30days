#include <bits/stdc++.h>

using namespace std;

string get_binary(int n)
{
    string binary = "";
    while (n > 0)
    {
        binary = to_string(n%2)+binary;
        n = n / 2;
    }    
    return binary;
}

int get_consec(string binary)
{

    int max_consec = 0;
    int cur_count = 0;
    for (int i = 0; i < binary.length(); i++)
    {
        if (binary[i] == '1'){
            cur_count += 1;
            if (max_consec < cur_count)
                max_consec = cur_count;
        }
        else
            cur_count = 0;
    }

    return max_consec;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string bin = get_binary(n);
    int max_consec = get_consec(bin);
    cout << max_consec << endl;
    return 0;
}

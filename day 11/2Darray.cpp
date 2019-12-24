#include <bits/stdc++.h>

using namespace std;

/*
1 1 1 0 0 0     1 1 1  1 1 0
0 1 0 0 0 0       1      0
1 1 1 0 0 0     1 1 1  1 1 0  etc.
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
*/

int getHourGlassSum(vector<vector<int>> arr, int startX, int startY)
{
    int size = 3;
    int sum = 0;
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            
            if (j == 1){
                if (i == 1)
                {
                    sum += arr[j+startY][i+startX];
                }
            }
            else{
                sum += arr[j+startY][i+startX];
            }
        }
    }
    return sum;
}

int main()
{
    const int SIZE = 6;
    vector<vector<int>> arr(SIZE);
    for (int i = 0; i < SIZE; i++) {
        arr[i].resize(SIZE);

        for (int j = 0; j < SIZE; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int max = INT_MIN;
    const int LIMIT = 4;
    for (int i = 0; i < LIMIT; i++)
    {
        for (int j =0; j < LIMIT; j++)
        {
            int cur = getHourGlassSum(arr, i, j);
            if (cur > max){
                max = cur;
            }
        }
    }

    cout << max << endl;

    return 0;
}

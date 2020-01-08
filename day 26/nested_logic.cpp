#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

int* getDate()
{ 
    string str_date1;
    getline(cin, str_date1);
    // Used to split string around spaces. 
    istringstream ss(str_date1);
    int *dates = new int[3];
    int index = 0;
    // Traverse through all words 
    do { 
        // Read a word 
        int num; 
        ss >> num; 
        dates[index] = num;
        index++;
        // While there is more to read 
    } while (ss); 
    return dates;
} 

int getFine(int* returned, int* expected){
    if (expected[2] < returned[2])
        return 10000;
    else if ((expected[0] >= returned[0] && expected[1] >= returned[1])
        || expected[2] > returned[2]){
        return 0;
    }
    else if (expected[0] < returned[0] && expected[1] == returned[1])
        return 15*(returned[0]-expected[0]);
    else {
        return 500*(returned[1]-expected[1]);
    }
}

int main() {

    int* returned = getDate();
    int* expected = getDate();
    cout << getFine(returned, expected) << endl;

    return 0;
}

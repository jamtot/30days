#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    string S;
    cin >> S;

    try {
        int n = stoi(S);
        cout << n << endl;
    }
    catch (invalid_argument const &e) {
        // if it's not a valid number
        cout << "Bad String" << endl;
    }
    catch (std::out_of_range const &e) {
        // if it's out of the range of an integer
        cout << "Bad String" << endl;
    }
    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int n;
    string number;
    getline(cin, number);
    n = stoi(number);

    map<string, string> phone_book; 

    for (int i = 0; i < n; i++)
    {
        string name_n_num;
        getline(cin, name_n_num);

        string name = "";
        string number = "";
        string word = "";

        int count = 0;
        for (auto x : name_n_num) 
        { 
            if (x == ' ') 
            { 
                if (count == 0)
                    name = word;
                word = ""; 
            } 
            else
            { 
                word = word + x; 
            } 
            number = word;
        }  
        phone_book.insert(pair<string, string>(name, number)); 
    }

    vector<string> queries;
  
    string line;
    while(getline(cin,line))
    {
        if (line.empty())
        break;
        queries.push_back(line);
    }

    vector<string>::iterator it = queries.begin();
    for (;it != queries.end(); ++it){

        map<string,string>::iterator map_it = phone_book.find(*it);
        if(map_it != phone_book.end())
        {
            //element found;
            cout << *it << "=" << map_it->second << endl;
        } else
            cout << "Not found" << endl;
    }

    return 0;
}

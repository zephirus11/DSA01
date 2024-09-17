#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    bool flag = 1;
    vector<string> v;
    string pattern = "abba", s = "dog cat cat dog";
    string word;
    stringstream ss(s);
    while (ss >> word) {
        cout << word<<endl;
        v.push_back(word);
    }
    // check if size of pattern and vector is same or not
    if(v.size() != pattern.size())
    {
        flag = false;
    }
    map<char, string> m1;
    map<string, char> m2;
    for (int i = 0; i < pattern.size(); i++)
    {
        string w = v[i];
        char c = pattern[i];
        // this check that mapping is avl
        if(m1.find(c) != m1.end())
        {
            // but it is undesirable
            if(m1[c] != w)
            {
                flag = false;
            }
        }
        if(m2.find(w) != m2.end())
        {
            if(m2[w] != c)
            {
                flag = false;
            }
        }
        m1[c] = w;
        m2[w] = c;
    }
    cout << flag;
    return 0;
}

// m.find(x) if key found it returns an iterator that points to the key-value pair. 
// m.end() returns the iterator which is one past the last element of map. it does not point to valid key-value pair. this is why we use
// if(m.find(x) == m.end()) means that key x does not exist or valid in map.
// we should use .find() method only because it does not insert any key-value pair in map and prevents unexpected error it just searches the map for key existence.
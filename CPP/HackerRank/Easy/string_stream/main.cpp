// The task is here https://www.hackerrank.com/challenges/c-tutorial-stringstream/problem

#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

// Splits string str to integers by comma delimiter
// and return a vector of that integers
vector <int> parseInts(string str) {
    vector <int> v;   // the vector which we are going to return
    char delim = ','; // delimiter
    int number;       // temprorary integer

    // putting input string to a string stream
    stringstream ss;
    ss << str;

    //
    while(1) {
        ss >> number;        // Firstly read the integer
        v.push_back(number); // and then put it to the vector.
        if (!ss.eof())       // If there is a data in the stream,
            ss >> delim;     // we skip comma
        else                 // If there is no any data instream,
            break;           // we break the loop
    }
    return v;
}

int main() {
    string str;
    cin >> str;
    vector <int> integers = parseInts(str);
    for(unsigned i = 0; i < integers.size(); i++) {
        cout << integers[i] << endl;
    }

    return 0;
}

// The task is here https://www.hackerrank.com/challenges/attribute-parser/problem

#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

// organize the input of HRML-code
// Input: N - number of lines in the HRML source program
// Output: stringsteam of inputed data
stringstream HRML_input(int N) {
    stringstream ss;
    for (int i = 0; i <= N; i++) {
        string str;
        getline(cin, str);
        str.append(" ");
        ss << str;
    }
    return ss;
}

map <string, string> HRML_parser(stringstream & ss) {
    map <string, string> data; // store parsed data
    vector <string> templ; // template for storing address of a tag
    // addr - address of a tag
    // str - temprorary string for getting data from ss
    // prop - property of a tag
    // attribute - property of an attribute
    string addr, str, attribute, prop;

    // do the loop while we can read the data from the stringstream
    while (ss >> str) {
        addr.clear();

        if (str[0] == '<' && str.back() == '>' && str[1] != '/') { // if the empty opening tag without any attributes
            str.assign(str.begin() + 1, str.end() - 1); // save the tag to vector 'templ'
            templ.push_back(str);
        }
        else if (str[0] == '<' && str[1] != '/') { // if the opening tag with attributes
            // save the tag to vector 'templ'
            str.assign(str.begin() + 1, str.end());
            templ.push_back(str);
            // fill address string using templ vector adding dots between tags
            addr.append(templ[0]);
            for (unsigned i = 1; i < templ.size(); i++)
                addr.append("." + templ[i]);
            // parse the data inside the tag
            while (1) {
                attribute.clear();
                prop.clear();

                ss >> str; // read the first property
                prop = str;
                ss >> str; // skip '='
                ss >> str; // read the attriute

                if (str.back() == '>') { // if the last property
                    // add the property data to the map
                    attribute.append(str, 1, str.size() - 3);
                    data[addr + "~" + prop] = attribute;
                    break;
                }
                else { // if it's not last property
                    // add the property data to the map
                    attribute.append(str, 1, str.size() - 2);
                    data[addr + "~" + prop] = attribute;
                }
            }
        }
        else if (str[0] == '<' && str[1] == '/') // if the closing tag
            templ.pop_back();
    }
    return data;
}

// quiries processing for searching data in parsed HRML-code
// Input: data - parsed data, Q - number of queries
void query_processing(map <string, string> &data, int Q) {
    // searching data in the map and if it is finded, puts the information in stdout
    // otherwise prints "Not Found"
    for (int i = 0; i < Q; i++) {
        string query;
        cin >> query;
        if (data.find(query) != data.end())
            cout << data[query] << endl;
        else
            cout << "Not Found!" << endl;
    }
}

int main()
{
    int N; // number of lines in the HRML source program
    int Q; // number of queries
    cin >> N >> Q;

    stringstream ss = HRML_input(N);
    map <string, string> data = HRML_parser(ss);

    /*
        // Uncomment this code if you want to print the parsed data
        cout << endl;
        for (auto const& pair: data)
            cout << pair.first << " : " << pair.second << endl;
        cout << endl;
    */

    query_processing(data, Q);

    return 0;
}

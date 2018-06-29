#include <iostream>

#include "mystring.h"

using namespace std;

int main() {
    MyString s1 = "Hello";
    MyString s2 = " world";
    s1.append(s2);
    s1.print();
    return 0;
}

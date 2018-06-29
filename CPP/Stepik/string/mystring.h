
#ifndef MYSTRING_H
#define MYSTRING_H

#include <cstddef> // size_t
#include <cstring> // strlen, strcpy
#include <iostream>

using namespace std;

class MyString {
public:
    MyString(const size_t size);
    MyString(const char *str = "");
    MyString(size_t n, char c);
    MyString(MyString const & myS); //copy constructor

    ~MyString();

    MyString & operator =(MyString const & myS); // for avoiding problems with memory

    void append(MyString &other);
    size_t length() const;
    char get(size_t pos) const;
    char &get(size_t pos);
    bool equal(const MyString &other) const;
    void print() const;

private:
    void resize(size_t nsize);
    void swap (MyString & myS);

    size_t size_;
    char *data_;
};

#endif // MYSTRING_H


#ifndef MYSTRING_H
#define MYSTRING_H

// My own variant of String class.
// During the lessons we got tasks about creating
// the functions in the context of the lessons

#include <cstddef> // size_t
#include <cstring> // strlen
#include <iostream>

using namespace std;

class MyString {
public:
    MyString(const size_t size); // Creates class using only size of the new string. String data initializes 0.
    MyString(const char *str = ""); // Creates class using data from C-style string
    MyString(size_t n, char c); // Create string of symbols c with size n
    MyString(MyString const & myS); //copy constructor for avoiding problems with memory

    ~MyString();

    MyString & operator =(MyString const & myS); // for avoiding problems with memory

    void append(MyString &other); // Appends new string to the current
    size_t length() const; // Returns the length of the string
    char get(size_t pos) const; // Returns the symbol in the position pos
    char &get(size_t pos); // Return reference to the symbol. It is need for editing the symbol in the position
    bool equal(const MyString &other) const; // Compares the current string and the string other. If they are equal, returns true
    void print() const; // Put the string data in stdout

private:
    void resize(size_t nsize); // change the size of the string data
    void swap (MyString & myS); // swap all the data of the current string and myS

    size_t size_; // size of the string
    char *data_; // data where stores symbols of the string
};

#endif // MYSTRING_H

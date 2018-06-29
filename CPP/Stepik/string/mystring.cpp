
#include <cstddef> // size_t
#include <cstring> // strlen, strcpy
#include <iostream>

#include "mystring.h"

MyString::MyString(const size_t size) :
    size_(size)
{
    for (size_t i = 0; i != size; i++)
        data_[i] = 0;
}

MyString::MyString(const char *str) :
    size_(strlen(str)),
    data_(new char[size_+1])
{
    for (size_t i = 0; i <= size_; i++)
        this->data_[i] = str[i];
}

MyString::MyString(size_t n, char c) :
    size_(n),
    data_(new char[size_+1])
{
    for (size_t i = 0; i < size_; i++)
        this->data_[i] = c;
    data_[size_] = '\0';
}

MyString::MyString(const MyString &myS)
    :MyString(myS.data_)
{}

MyString::~MyString() {
    delete [] data_;
}

MyString & MyString::operator=(MyString const & myS) {
    if (this != &myS)
        MyString(myS).swap(*this);
    return *this ;
}

void MyString::swap(MyString &myS) {
    std::swap(size_, myS.size_);
    std::swap(data_, myS.data_);
}

void MyString::append(MyString &other) {
    size_t size_tmp = size_;
    resize(other.size_ + size_);
    for (size_t i = size_tmp; i < other.size_ + size_tmp; i++)
        data_[i] = other.data_[i - size_tmp];
    data_[size_] = '\0';
}

size_t MyString::length() const {
    return size_;
}
char & MyString::get(size_t pos) {
    return data_[pos];
}

char MyString::get(size_t pos) const {
    return data_[pos];
}

bool MyString::equal(const MyString &other) const {
    if (this->size_ == other.size_) {
        for (size_t i = 0; i < size_; i++) {
            if (this->data_[i] != other.data_[i])
                return false;
        }
        return true;
    }
    else return false;
}

void MyString::print() const {
    for (size_t i = 0; i < size_; i++)
        cout << data_[i];
    cout << endl;
}

void MyString::resize(size_t nsize)
{
    MyString t(nsize);
    size_t n = nsize > size_ ? size_ : nsize;
    for (size_t i = 0; i != n; ++i)
        t.data_[i] = data_[i];
    swap(t);
}

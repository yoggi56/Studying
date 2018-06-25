// The task is here https://www.hackerrank.com/challenges/box-it/problem

#include<bits/stdc++.h>

using namespace std;

class Box {
public:
    Box() :
        l(0), b(0), h(0)
    {}
    Box(int l, int b, int h) :
        l(l), b(b), h(h)
    {}
    Box(Box &bx) :
        l(bx.getLength()),
        b(bx.getBreadth()),
        h(bx.getHeight())
    {}

    int getLength() {
        return l;
    }

    int getBreadth () {
        return b;
    }

    int getHeight () {
        return h;
    }

    long long CalculateVolume() {
        return (long long)l * b * h;
    }

    bool operator<(Box &bx) {
        if ((l < bx.getLength())
                || (b < bx.getBreadth() && l == bx.getLength())
                || (h < bx.getHeight() && l == bx.getLength() && b == bx.getBreadth()))
            return true;
        else return false;
    }

    friend ostream& operator<<(ostream &out, Box &bx) {
        out <<  bx.getLength() << " " << bx.getBreadth() << " " << bx.getHeight();
        return out;
    }

private:
    int l,b,h;

};

void check2()
{
    int n;
    cin>>n;
    Box temp;
    for(int i=0;i<n;i++)
    {
        int type;
        cin>>type;
        if(type ==1)
        {
            cout<<temp<<endl;
        }
        if(type == 2)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            temp=NewBox;
            cout<<temp<<endl;
        }
        if(type==3)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            if(NewBox<temp)
            {
                cout<<"Lesser\n";
            }
            else
            {
                cout<<"Greater\n";
            }
        }
        if(type==4)
        {
            cout<<temp.CalculateVolume()<<endl;
        }
        if(type==5)
        {
            Box NewBox(temp);
            cout<<NewBox<<endl;
        }

    }
}

int main()
{
    check2();
}

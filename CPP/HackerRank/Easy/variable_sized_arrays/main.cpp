/*

    The task is here https://www.hackerrank.com/challenges/variable-sized-arrays/problem

*/
#include <iostream>

using namespace std;

int main()
{
    unsigned n_a; // the number of variable-length arrays
    int q; // the number of queries
    cin >> n_a >> q;

    unsigned n_k; // the number of elements in subarrays
    int ** a = new int * [n_a]; // matrix a

    // input the data for subarrays and create them dynamically
    for (unsigned i = 0; i != n_a; i++) {
        cin >> n_k;
        a[i] = new int [n_k];
        for (unsigned j = 0; j != n_k; j++) {
            cin >> a[i][j];
        }
    }

    // input queries and output the result
    unsigned i, j;
    for (int s = 0; s < q; s++) {
        cin >> i >> j;
        cout << a[i][j] << endl;
    }

    return 0;
}

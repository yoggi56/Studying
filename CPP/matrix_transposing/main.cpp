#include <iostream>

using namespace std;

// Memory allocation for matrix with a rows and b columns
int ** create_matrix(size_t a, size_t b) {
    int ** m = new int * [a];
    m[0] = new int[a * b];
    for (size_t i = 1; i != a; ++i)
        m[i] = m[i - 1] + b;
    return m;
}

// Deleting matrix m
void delete_matrix(int ** m) {
    delete [] m[0];
    delete [] m;
}

// Matrix transposing
// Input: m - original matrix, a - rows, b - columns
// Output: transposed matrix
int ** transpose(const int * const * m, size_t a, size_t b) {
    int ** m_t = create_matrix(b, a);
    for (size_t i = 0; i != a; i++) {
        for (size_t j = 0; j != b; j++)
            m_t[j][i] = m[i][j];
    }

    return m_t;
}

// Use this function if you want to print your matrix in stdout
// Input: m - your matrix, a - rows, b - columns
void print_matrix(int ** m, size_t a, size_t b) {
    for (size_t i = 0; i != a; i++) {
        for (size_t j = 0; j != b; j++)
            cout << m[i][j] << " ";
        cout << endl;
    }
}

int main() {
    size_t a = 5, b = 10; // rows and columns
    int ** matrix = create_matrix(a, b); // creating original matrix

    //initializing and printing the matrix
    for (size_t i = 0; i != a; i++) {
        for (size_t j = 0; j != b; j++)
            matrix[i][j] = j;
    }
    cout << "Original matrix:" << endl;
    print_matrix(matrix, a, b);

    // creating, transposing and printing new matrix
    cout << "\nTransposed matrix:" << endl;
    int ** transposed_matrix = create_matrix(b, a);
    transposed_matrix = transpose(matrix, a, b);
    print_matrix(transposed_matrix, b, a);

    // freeing the memory
    delete_matrix(matrix);
    delete_matrix(transposed_matrix);
    return 0;
}

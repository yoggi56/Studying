/*
    Develop the function swap_min that takes for the input 2d-massive integer
    numbers, finds in the massive the row which contains minimal value in the whole
    massive and then swap this row with the first row of this massive.
    Try to swap the rows without swaping each element.

    Реализуйте функцию swap_min, которая принимает на вход двумерный массив
    целых чисел, ищет в этом массиве строку, содержащую наименьшее среди всех
    элементов массива значение, и меняет эту строку местами с первой строкой массива.

    Подумайте, как обменять строки массива, не обменивая элементы строк по-отдельности.
*/

#include <iostream>
#include <ctime>

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

// Find in a matrix the row with the least element and then
// swap that row with the first one
void swap_min(int * m[], unsigned rows, unsigned cols)
{
    int * row = new int[cols];
    int min = m[0][0];
    int min_row = 0;

    for (size_t i = 0; i != rows; ++i)
        for (size_t j = 0; j != cols; ++j)
            if (m[i][j] < min) {
                min = m[i][j];
                min_row = i;
            }

    row = m[min_row];
    m[min_row] = m[0];
    m[0] = row;

    cout << "\nThe row with the least element is " << min_row << ":" << endl;
    for (unsigned i = 0; i != cols; i++)
        cout << row[i] << " ";
    cout << endl;
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

int main()
{
    srand(time(0));
    size_t a = rand() % 10 + 2, b = rand() % 10 + 2; // randomly initialized rows and columns
    int ** matrix = create_matrix(a, b); // creating original matrix

    // Initializing and printing the matrix
    for (size_t i = 0; i != a; i++) {
        for (size_t j = 0; j != b; j++)
            matrix[i][j] = rand() % 100;
    }
    cout << "Original matrix:" << endl;
    print_matrix(matrix, a, b);

    // Swapping the minimal row with the first row and then printing
    swap_min(matrix, a, b);

    cout << "\nSwapped matrix:" << endl;
    print_matrix(matrix, a, b);

    delete_matrix(matrix);

    return 0;
}

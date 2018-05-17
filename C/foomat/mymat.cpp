#include "mymat.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>


MyMat::MyMat()
{
}

MyMat::MyMat(int r, int c)
{
    init(r, c);
}

MyMat::MyMat(const MyMat& M)
{
    init(M.row, M.col);
    memcpy(buffer, M.buffer, sizeof(int)*row*col);
}

MyMat::~MyMat()
{
    if (buffer != NULL) {
        free(buffer);
    }
}

void MyMat::init(int r, int c)
{
    row = r;
    col = c;
    buffer = (int*)malloc(sizeof(int)*row*col);
    bzero(buffer, sizeof(int)*row*col);
}

int MyMat::at(int r, int c) const
{
    if (r >= row) {
        throw "r is out-of-bound";
    }
    if (c >= col) {
        throw "c is out-of-bound";
    }
    return buffer[r*col + c];
}

void MyMat::set(int r, int c, int v)
{
    if (r >= row) {
        throw "set: r is out-of-bound";
    }
    if (c >= col) {
        throw "set: c is out-of-bound";
    }
    buffer[r*col + c] = v;
}

void MyMat::dump() const
{
    if (row == 0 || col == 0) {
        printf("Empty\n");
        return;
    }
    for (int y = 0; y < row; ++y) {
        for (int x = 0; x < col; ++x) {
            int p = at(y, x);
            printf("%d ", p);
        }
        printf("\n");
    }
    printf("\n");
}

void MyMat::dot(int n)
{
    for (int y = 0; y < row; ++y) {
        for (int x = 0; x < col; ++x) {
            int p = at(y, x);
            set(y, x, p*n);
        }
    }
}

int MyMat::dotProduct(int mr, int nc, const MyMat& N) const
{
    // M row vs N col
    int sum = 0;
    for (int i = 0; i < col; ++i) {
        sum += at(mr, i) * N.at(i, nc);
    }
    return sum;
}

MyMat MyMat::cross(const MyMat& N)
{
    if (row != N.col || col != N.row) {
        throw "matrix size not match";
    }
    MyMat m(row, N.col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < N.col; j++) {
            int val = dotProduct(i, j, N);
            //printf("i,j,v: %d, %d, %d\n", i, j, val);
            m.set(i, j, val);
        }
    }

    return m;
}

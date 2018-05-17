#ifndef __MY_MAT_H__
#define __MY_MAT_H__

class MyMat
{

public:
    MyMat();
    MyMat(int r, int c);
    MyMat(const MyMat& M);
    ~MyMat();

    int at(int r, int c) const;
    void set(int r, int c, int v);
    void dump() const;
    void dot(int n);
    MyMat cross(const MyMat& N);
    int dotProduct(int mr, int nc, const MyMat& N) const;

    int row = 0;
    int col = 0;

    //MyMat operator=(const MyMat& m);

protected:
    void init(int r, int c);

private:
    int *buffer = nullptr;
};


#endif  // __MY_MAT_H__

#include <iostream>
#include <vector>

using namespace std;

void operate_elem(vector<int>::iterator& it)
{
    if (*it % 2 == 1) {
        (*it) ++;
    }
}

void process_vector(vector<int>& v)
{
    vector<int>::iterator it;
    for (it = v.begin(); it != v.end(); ++it) {
        operate_elem(it);
        cout << *it << " ";
    }
    cout << endl;
}

void show_vector(const vector<int>& v)
{
    for (size_t i=0; i<v.size(); ++i) {
        cout << v.at(i) << " ";
    }
    cout << endl;
}

void gothrough_vector2d(vector<vector<int>>& v2d)
{
    vector<vector<int>>::iterator it;
    for (it = v2d.begin(); it != v2d.end(); ++it) {
        process_vector(*it);
    }
}

int main()
{
    vector<int> ps1 = {1,2,3,5,7};
    vector<int> ps2 = {11,13,17,19,23};

    vector< vector<int> > p2d;

    p2d.push_back(ps1);
    p2d.push_back(ps2);

    gothrough_vector2d(p2d);
    cout << "after processing..." << endl;
    show_vector(ps1);
    show_vector(p2d.at(0));

    return 0;
}

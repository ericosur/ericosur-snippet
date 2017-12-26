#include <iostream>
#include <string>

// get dirname by using std::string::rfind()

using namespace std;

#define SAMPLE_STRING   "/home/rasmus/Videos/misc-videos/youtube/阿基師偷呷步-蕃茄妙蛋.flv"

bool split_path(const string& s, string& dirname, string& filename)
{
   char sep = '/';

   size_t i = s.rfind(sep, s.length());
   if (i != string::npos) {
      filename = s.substr(i+1, s.length() - i);
      dirname = s.substr(0, i);
      return true;
   }

   return false;
}

void do_test(const string& str)
{
    string dirname;
    string filename;
    if (split_path(str, dirname, filename)) {
        cout << "fpath: " << str << endl
            << "dirname: " << dirname << endl
            << "filename: " << filename << endl;
    } else {
        cout << "cannot split path...";
    }
}

int main(int argc, char** argv)
{
    string fpath;

    if (argc <= 1) {
        do_test(SAMPLE_STRING);
        return 0;
    }

    for (int i = 1; i < argc; ++i) {
        do_test(argv[i]);
        cout << endl;
    }

    return 0;
}

#include <iostream>
#include "argh.h"

using namespace std;

int main(int, char* argv[])
{
    argh::parser cmdl(argv);

    if (cmdl[{ "-v", "--verbose" }])
        cout << "Verbose, I am.\n";

    float threshold;
    // Check for missing param and/or bad (inconvertible) param value
    if (!(cmdl({ "-t", "--threshold"}) >> threshold)) {
        cerr << "Must provide a valid threshold value! Got '" << cmdl("threshold").str() << "'" << endl;
    }
    else {
        cout << "Threshold set to: " << threshold << '\n';
    }


    return EXIT_SUCCESS;
}

#include <iostream>
#include <string>

// list standard-library names we will be using
using std::cout; using std::cin;
using std::endl; using std::string;

int main()
{
    int product = 10;
    for (int i = 10; i != 1; --i) {
        product = product * (i-1);
    }
    cout << product << endl;
    return 0;
}

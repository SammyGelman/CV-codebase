#include <iostream>
#include <string>

// list standard-library names we will be using
using std::cout; using std::cin;
using std::endl; using std::string;

int main()
{
    for (int nums = 15;nums >= 0; --nums){
        cout << nums - 5 << endl;
    }
return 0;
}

#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
// #include <ostream>

using std::cin;     using std::cout;  
using std::endl;    using std::setprecision; 
using std::string;  using std::streamsize; 
using std::vector;  using std::sort;
using std::copy;
int main ()
{
    // get values for the quarterly
    vector<int> vect {5,3,3,3,1,1,1,4,5,6,4,3,2,3,5,4,6,3,4,5,3,2,2,4,5,6,6,1,2,2,2,0,0,0};

    // first save the size as a variable
    typedef vector<double>::size_type vec_sz;
    vec_sz size = vect.size();

    // sort by using a library defined function
    sort(vect.begin(), vect.end());

    // define remainder for later use
    int remain;
    remain = size % 4;

    // define quarter size accounting for the error    
    vec_sz quarter;
    quarter = remain == 0 ? size/4 
                          : (size - remain) / 4;

    // start to print out the quarters
    int q_count = 0;
 
    // print tests
    // cout << "vect[0]: " << vect[0]; 
    cout << "remain: " << remain << endl; 
    cout << "quarter: " << quarter << endl; 

    while (q_count != 4) {
        cout << "quarter " << q_count +1 << ": ";        
        if (remain != 0) {
            for (int i=0; i != quarter + 1; ++i)
                cout << vect[i + q_count*quarter] << ' ';
                remain -= 1;
        } else {
            for (int i=0; i != quarter; ++i)
            cout << vect[i + q_count*quarter] << ' ';
        } 
        cout << endl;
        q_count += 1;
    }
    return 0;
}
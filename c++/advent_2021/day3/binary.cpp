#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>
#include <sstream>
#include <typeinfo>


using std::cin;     using std::cout;  
using std::endl;    using std::setprecision; 
using std::string;  using std::streamsize; 
using std::vector;  using std::sort;
using std::__cxx11::stoi;

int main ()
{
    std::ifstream in ("input.txt");

    // initialize vector of input data 
    vector<string> input{
        std::istream_iterator<string>(in),
        std::istream_iterator<string>()
    };

    int n = input[0].size();
    vector<int> vect(n, 0);
    
    for (auto iter = input.begin(); iter != input.end(); iter++) {
        cout << *iter << endl;
        for (int i = 0; i < n; i++) {
            vect[i] += ((*iter)[i] - 48);
           }
    }
    
    vector<int> gamma_vec(n, 0);
    vector<int> epsilon_vec(n, 0);
    int idx; 
    int gamma;
    int epsilon; 
    int count = 0;
    int len = input.size();

    for (auto iter = vect.begin(); iter != vect.end(); iter++) {
        if (*iter >= (len/2)) {
            gamma_vec[idx] = 1; 
            idx += 1;
        } else {
            epsilon_vec[idx] = 1;
            idx += 1;
        }
    }

    for (auto elem : vect) {
        cout << elem << " ";
    }


    for (auto elem : gamma_vec) {
        cout << elem << " ";
    } 

    for (auto elem : epsilon_vec) {
        cout << elem << " ";
    }
    return 0;
}

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
    int l = input.size();
    vector<int> vect(n, 0);
    
    for (auto iter = input.begin(); iter != input.end(); iter++) {
        for (int i = 0; i < n; i++) {
            vect[i] += ((*iter)[i] - 48);
           }
    }

    vector<int> oxygen_key(n, 0);
    vector<int> co2_key(n, 0);
 
    for (int i = 0; i < n; i++) {
        if (vect[i] >= (l/2)) {
            oxygen_key[i] = 1;
        } else {
            co2_key[i] = 1;
        }
    }

    int gamma;
    int epsilon; 
    int count = 0;
    
    vector<int> oxygen_score(l, 0);
    vector<int> co2_score(l, 0);

    for (auto iter = input.begin(); iter != input.end(); iter++) {
        for (int i = 0; i < n; i++) {
            cout << "input value" << endl;
            cout << (*iter)[i] << endl;
            cout << "o2 value" << endl;
            cout << oxygen_key[i] << endl;
            if ((*iter)[i] == oxygen_key[i]) {
                oxygen_score[count] += 1;
                cout << "o2 score" << endl;
                cout << oxygen_score[count] << endl;
            } else {
                co2_score[count] += 1;
            }
        }
        count += 1;
    }

    cout << oxygen_score[43] << endl;
    cout << co2_score[43] << endl;

    return 0;
}

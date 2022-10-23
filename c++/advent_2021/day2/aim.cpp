#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>


using std::cin;     using std::cout;  
using std::endl;    using std::setprecision; 
using std::string;  using std::streamsize; 
using std::vector;  using std::sort;

int main ()
{
    std::ifstream in ("input.txt");

    // initialize vector of input data 
    vector<string> input{
        std::istream_iterator<string>(in),
        std::istream_iterator<string>()
    };

    int dist = 0;
    int depth = 0;
    int aim = 0;

    for (auto iter = input.begin() + 1; iter != input.end() + 1; iter += 2) {
        if (*(iter - 1) == "forward") {
            dist += stoi(*iter);
            depth += (aim * stoi(*iter));
        } else if  (*(iter - 1) == "down") {
            aim += stoi(*iter);
        } else {
            aim -= stoi(*iter);
        }
    }
    
    cout << "Final Distance: "
        << dist 
        << ".\nFinal Depth: "
        << depth
        << ".\nFinal Answer: "
        << dist*depth;
    return 0;
}

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
    vector<int> input{
        std::istream_iterator<int>(in),
        std::istream_iterator<int>()
    };

    int answer = 0;
    int counter = 0;
    int window_counter = 0;

    // create vector fo new input
    vector<int> new_input;

    // get length of input
    typedef vector<int>::size_type input_len;
    input_len len = input.size();

     // loop over input
    for (const auto& value: input){
        if (window_counter < (len - 2)){
                new_input.push_back(value + input[window_counter + 1] + input[window_counter + 2]);
                window_counter += 1;
        } 
    }

     // get new length of input
    typedef vector<int>::size_type input_len;
    input_len new_len = new_input.size();


    // loop over input
    for (const auto& value: new_input){
        if (counter < (new_len - 1)){
            if (value < new_input[(counter + 1)]) {
                answer += 1;
                counter += 1;
            } else {
                counter += 1;
            }
        } else {
            cout << answer;
        }

    }
    
    cout << "Answer: " << answer << "\n Counter (should be 1998): " << counter;
    
    return 0;
}
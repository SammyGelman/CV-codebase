#include <iostream>
#include <string>

// list standard-library names we will be using
using std::cout; using std::cin;
using std::endl; using std::string;

int main()
{
    // output shape choices
    cout << "Please submit two numbers: " << endl 
    << "First number: ";
    
    // set shape input
    int first;
    cin >> first;
    
    cout << "Second number: ";
    
    int second;
    cin >> second;
    
    if (first == second){
        cout << "These values are equal, please enter non-equal numbers." << endl;
        
        cout << "Second number: " << endl;
     
        cin >> second;
        }
    
    // check shape
    if (first >= second){
        // output dimension options
        cout << first << " is greater than " << second << "." << endl;
    } else {
        cout << second << " is greater than " << first << "." << endl;
    }
    return 0;
}
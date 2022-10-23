#include <iostream>
#include <string>

// list standard-library names we will be using
using std::cout; using std::cin;
using std::endl; using std::string;

int main()
{
    cout<<"Please enter your first name: ";
    string name; //define name
    cin >> name; //read into

    cout<<"Enter amount of space above and below name: ";
    int pad;
    cin >> pad;

    const string greeting = "Hello, " + name + "!";

    //write a flexible definition for the total number of rows present in the output
    //number of blanks
    const int side_pad = 5;

    // total number of rows to write
    const int rows = pad*2 + 3;
    
    // set uniform column size for the banner
    const string::size_type cols = greeting.size() + side_pad*2 + 2;
    const string space = space(greeting.size()," ");
    // seperate the output and the input
    cout << endl;
    
    // invariant: we have written r rows so far
    for (int r = 0; r != rows; ++r) {
    
        // filling the columns properly using a while loop
        string::size_type c = 0;
    
        // invarient: we have written c characters in the current row
        while (c != cols) {
            // do we write the greeting?
            if (r == pad + 1 && c == side_pad +1 ){
                cout << greeting;
                c += greeting.size();
            } else{
            // are we on the border?
            if (r == 0 || r == rows -1 ||
                c == 0 || c == cols-1) 
                cout << '*'; 
            else 
                cout << space;
                c += greeting.size();
            // adjust the value of c to maintain the invariant
            ++c;
            }
        }
        cout << endl;
    }
    return 0;
}

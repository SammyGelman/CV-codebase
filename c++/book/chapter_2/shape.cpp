#include <iostream>
#include <string>

// list standard-library names we will be using
using std::cout; using std::cin;
using std::endl; using std::string;

int main()
{
    // output shape choices
    cout << "Please select shape option: " << endl 
    << "Rectangle: 1" << endl
    << "Square: 2" << endl
    << "Triangle: 3" << endl;
    
    // set shape input
    int shape;
    cin >> shape;
    
    // check shape
    if (shape == 1){
        // output dimension options
        cout << "Please insert length: " << endl;
        
        // set shape input
        int length;
        cin >> length;
        
        cout << "Please insert height: " << endl;
        
        // set shape input
        int height;
        cin >> height;
    
    const string row(length,'*');
    
    for (int i =0; i != height; i++){
        cout << row << endl;
    }
    }
    
    if (shape == 3){
        // output dimension options
        cout << "Please insert base size: " << endl;
        
        // set shape input
        int base;
        cin >> base;
        
        for (int i=1; i != base+1; i++){
            cout << string(i, '*') << endl;
        }
    }
    
    if (shape == 2){
        // output dimension options
        cout << "Please insert side length: " << endl;
        
        // set shape input
        int length;
        cin >> length;
        
        const string row(length,'*');
    
        for (int i =0; i != length; i++){
          cout << row << endl;
        }
    }
    return 0;
}
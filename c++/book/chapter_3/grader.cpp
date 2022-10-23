#include <iomanip>
#include <ios>
#include <iostream>
#include <string>

using std::cin;     using std::cout;  
using std::endl;    using std::setprecision; 
using std::string;  using std::streamsize; 

int main ()
{
    // ask for and read the students name
    cout << "Please enter your first name: ";
    
    string name;
    cin >> name;
    cout << "Hello " + name + "!" << endl;

    // ask for and read final and midterm grades
    cout << name + " please enter your midterm and final grades: ";
    double midterm, final;
    cin >> midterm >> final;

    // ask for and read HW grades
    cout << name + " please enter your all of your " 
    "homework grades followed by end-of-file: ";

    // numbers to count the amount of hw and tally pre-avg
    int count = 0;
    double sum = 0;

    // var to hold cin for hw grades
    double x;

    // invariant
    // we have read count grades so far
    // sum is the sum of the first count grades
    while (cin >> x) {
        ++count;
        sum += x;
    }    

    // return grade for course
    streamsize prec = cout.precision();
    cout << "Your final grade is: "
        << 0.2*midterm + 0.4*final + 0.4*sum/count
        << setprecision(prec) << endl;

    return 0;
}
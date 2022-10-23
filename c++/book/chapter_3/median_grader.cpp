#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using std::cin;     using std::cout;  
using std::endl;    using std::setprecision; 
using std::string;  using std::streamsize; 
using std::vector;  using std::sort;

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
    vector<double> homework;

    // invariant
    // homework contains all the homework grades read so far 
    while (cin >> x) 
        homework.push_back(x);


    // compute the median homework grade
    // first save the size as a variable
    typedef vector<double>::size_type vec_sz;
    vec_sz size = homework.size();

    // abort program in the event that hw grades were not given
    if (size == 0){
        cout << "Please try again by entering proper homework grades!" << endl;
        return 1;
    }

    // next order the hw vector
    // we can do so by using a librar defined function
    sort(homework.begin(), homework.end());

    vec_sz mid = size/2;
    double median;

    median = size % 2 == 0 ? (homework[mid] + homework[mid -1]) / 2
                           : homework[mid];

    // return grade for course
    streamsize prec = cout.precision();
    cout << "Your final grade is: "
        << 0.2*midterm + 0.4*final + 0.4*median
        << setprecision(prec) << endl;

    return 0;
}
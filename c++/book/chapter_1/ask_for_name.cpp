// ask a person's name and greet them

#include <iostream>
#include <string>

int main()
{
    //ask for first name
    std::cout<<"Please enter your first name: ";
    
    // read the name
    std::string name; //define name
    std::cin >> name; //read into

    //write greeting
    std::cout<<"Hello, " << name << "!" <<std::endl;
    return 0;
}


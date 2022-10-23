#include <iostream>
#include <string>

int main()
{
    //ask for first name
    std::cout<<"Please enter your first name: ";
    
    // read the name
    std::string name; //define name
    std::cin >> name;
    std::cout << "Hello," << name
        << std::endl << "And what is yours?";
    std::cin >> name;
    std::cout << "Hello," << name
        << ", nice to meet you.";
    return 0;
}

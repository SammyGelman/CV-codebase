#include <iostream>
#include <string>

int main()
{
    std::cout<<"Please enter your first name: ";
    std::string name; //define name
    std::cin >> name; //read into

    const std::string greeting = "Hello, " + name + "!";
    
    // build the fourth and fifth line
    const std::string spaces(greeting.size(),' ');
    const std::string second = "* " + spaces + " *";
     
    // build the second and forth lines
    const std::string first(second.size(),'*');

    // write it all
    std::cout << std::endl;
    std::cout << first << std::endl;
    std::cout << second << std::endl;
    std::cout << "* " << greeting << " *"<< std::endl;
    std::cout << second << std::endl;
    std::cout << first << std::endl;

    return 0;
}

#include <iostream>
#include "Repository/RepositoryInMemory.h"
#include "Domain/Product.h"
#include "Tests/Tests.h"
#include "Service/Service.h"
#include "UserInterface/UserInterface.h"
#include <fstream>
using namespace std;
int main() {
    //TestAll();
    fstream file;
    file.open("test.txt", ios::in);
    file.open("test.txt", ios::out);
    file.close();
    RepositoryFile<Product> repo("test.txt");
    Service<Product> service(repo);
    UserInterface UI(service);
    UI.RunMenu();
    return 0;
}

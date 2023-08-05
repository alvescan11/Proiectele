//
// Created by Sergiu on 26.04.2022.
//

#ifndef MAIN_CPP_USERINTERFACE_H
#define MAIN_CPP_USERINTERFACE_H
#include "../Service/Service.h"
#include <map>
class UserInterface {
private:
    Service<Product> service;
public:
    UserInterface(const Service<Product> &_service);
    void RunMenu();
    void MenuCoin(map<int, int>& myCoin);
    void MenuProduct(vector<Product>& myProduct);
    void MenuUser(map<int, int>& myCoin,  map<string ,int>& myCount);
    void CoinRead(map<int, int>& myCoin);
    void CoinWrite(map<int, int> myCoin);
    void CountWrite( map<string ,int> myCount);
    void RadomGenerate(map<int, int>& myCoin, map<string ,int>& myCount);
    void ProductRead();
    void ProductWrite();
    void Menu(string _command);
};


#endif //MAIN_CPP_USERINTERFACE_H

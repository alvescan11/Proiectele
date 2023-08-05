//
// Created by Sergiu on 26.04.2022.
//

#include <algorithm>
#include "UserInterface.h"

UserInterface::UserInterface(const Service<Product> &_service) {
    this->service = _service;
}

void UserInterface::RunMenu() {
    bool ok = true;
    map<int, int> myCoin;
    map<string ,int> myCount;
    vector<Product> myProduct;
    while(ok)
    {
        Menu(" ");
        string command;
        cin >> command;
        if(command == "coin") {
            MenuCoin(myCoin);
        }
        else
        if(command == "product")
        {
            MenuProduct(myProduct);
        }
        else
        if(command == "user")
        {
            MenuUser(myCoin, myCount);
        }
        else
        if(command == "exit")
            ok = false;
        else
            cout << "Try another command" << endl;
    }
}

void UserInterface::CoinRead(map<int, int>& myCoin) {
    int s[4] = {1, 5, 10, 50};
    int value;
    myCoin.clear();
    for(auto& i: s){
        cout << i << " Bani:"; cin >> value;
        myCoin.emplace(i, value);
    }
}

void UserInterface::CoinWrite(map<int, int> myCoin) {
    for(auto& i: myCoin)
        cout << i.first << " Bani/" << "Count: " << i.second << endl;
}

void UserInterface::Menu(string _command) {
    if(_command == "coin") {
        cout << "1. Add some coins" << endl;
        cout << "2. Print some coins" << endl;
        cout << "x. Exit" << endl;
    }
    else
    if(_command == "product")
    {
        cout << "1. Add some products" << endl;
        cout << "2. Print some products" << endl;
        cout << "3. Update a product" << endl;
        cout << "4. Delete a product" << endl;
        cout << "x. Exit" << endl;
    }
    else
    if(_command == " ")
    {
        cout << "coin/product/user/exit" << endl;
    }
    else
    if(_command == "user")
    {
        cout << "1. Buy product" << endl;
        cout << "2. Random Generate" << endl;
        cout << "x. Exit" << endl;
    }
}

void UserInterface::ProductRead() {
    int size;
    cin >> size;
    for(int i = 0; i < size; i++){
        Product p;
        cout << "Product id: " << p.getIdUnic() + 1 << endl; cin >> p;
        if(!service.CodeVerify(p.getCode())){
            Product newp(p.getIdUnic() + 1, p.getCode(), p.getName(), p.getPrice());
            service.AddProduct(newp);
        }
        else
            cout << "Product code already exist!";
    }

}

void UserInterface::ProductWrite() {
    for(auto& p: service.getAll())
        cout << p;
}

void UserInterface::MenuCoin(map<int, int>& myCoin) {
    bool ok = true;
    while(ok)
    {
        Menu("coin");
        char read;
        cin >> read;
        switch (read) {
            case '1':
                CoinRead(myCoin);
                break;
            case '2':
                CoinWrite(myCoin);
                break;
            case 'x':
                ok = false;
                break;
            default:
                cout << "Wrong option";
        }
    }

}

void UserInterface::MenuProduct(vector<Product>& myProduct) {
    bool ok = true;
    while(ok)
    {
        Menu("product");
        char read;
        cin >> read;
        switch (read) {
            case '1':
                ProductRead();
                break;
            case '2':
                ProductWrite();
                break;
            case '3':
            {Product r;
                cin >> r;
                int id;
                cout << "Enter the id product you want to update:";
                cin >> id;
                if(service.IdVerify(id)) {
                    Product p = service.getProductId(id);
                    service.UpdateProduct(p, r);
                }
                else
                    cout << "You can't update an invalid product" << endl;
                break;}
            case '4':
                int id;
                cout << "Enter the id product you want to delete:";
                cin >> id;
                if(service.IdVerify(id))
                {
                    service.DeleteProduct(id);
                }
                else
                    cout << "You can't delete an invalid product" << endl;
                break;
            case 'x':
                ok = false;
                break;
            default:
                cout << "Wrong option" << endl;
        }
    }
}

void UserInterface::MenuUser(map<int, int>& myCoin,  map<string ,int>& myCount) {
    bool ok = true;
    while(ok)
    {
        Menu("user");
        char read;
        cin >> read;
        switch (read) {
            case '1':
                int id;
                double money;
                ProductWrite();
                cout << "Enter the product id:";
                cin >> id;
                cout << "Enter the money:";
                cin >> money;
                service.BuyProduct(id, money, myCoin, " ");
                break;
            case '2':
                RadomGenerate(myCoin, myCount);
                break;
            case 'x':
                ok = false;
                break;
            default:
                cout << "Wrong option" << endl;
        }
    }
}

void UserInterface::RadomGenerate(map<int, int>& myCoin, map<string ,int>& myCount) {
    int size;
    cout << "Enter the number of entity do you want to generate:";
    cin >> size;
    cout << endl;
    service.RandomGenerate(size, myCoin, myCount);
    ProductWrite();
    cout << endl;
    CoinWrite(myCoin);
    cout << endl;
    CountWrite(myCount);
    cout << endl;
}

void UserInterface::CountWrite(map<string, int> myCount) {
    for(auto& i: myCount)
        cout << i.first << ": " << i.second << endl;
}

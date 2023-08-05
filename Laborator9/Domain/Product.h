//
// Created by Sergiu on 19.04.2022.
//

#ifndef LABORATOR9_PRODUS_H
#define LABORATOR9_PRODUS_H

#include <string>
#include <iostream>
using namespace std;
class Product {
private:
    string code;
    string name;
    double price;
    int id_unic;
public:
    static int id_aux;
    Product();
    Product(string _code, string _name, double _price);
    Product(int id, string _code, string _name, double _price);
    Product(const Product& p);
    virtual ~Product();
    int getIdUnic();
    string getCode();
    string getName();
    double getPrice();
    void setCode(string newCode);
    void setName(string newName);
    void setPrice(double newPrice);
    void Clear();
    Product& operator=(const Product& p);
    bool operator==(const Product& p);
    friend istream& operator>>(istream& is, Product& p);
    friend ostream& operator<<(ostream& os, Product& p);
};


#endif //LABORATOR9_PRODUS_H

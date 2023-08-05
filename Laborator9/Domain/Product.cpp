//
// Created by Sergiu on 19.04.2022.
//

#include "Product.h"
int Product::id_aux = 0;
Product::Product() {
    this->id_unic = id_aux;
    this->code = "";
    this->name = "";
    this->price = 0;
}

Product::Product(string _code, string _name, double _price) {
    this->id_unic = ++id_aux;
    this->code = _code;
    this->name = _name;
    this->price = _price;
}

Product::Product(const Product &p) {
    this->id_unic = p.id_unic;
    this->code = p.code;
    this->name = p.name;
    this->price = p.price;
}

string Product::getCode() {
    return this->code;
}

string Product::getName() {
    return this->name;
}

double Product::getPrice() {
    return this->price;
}

void Product::setCode(string newCode) {
    this->code = newCode;
}

void Product::setName(string newName) {
    this->name = newName;
}

void Product::setPrice(double newPrice) {
    this->price = newPrice;
}

int Product::getIdUnic() {
    return this->id_unic;
}

istream &operator>>(istream &is, Product& p) {
    cout << "Product Code:";
    is >> p.code;
    cout << "Product Name:";
    is >> p.name;
    cout << "Product Price:";
    is >> p.price;
    return is;
}

ostream &operator<<(ostream &os, Product &p) {
    os << "Product Id: " << p.id_unic << " Product Code: " << p.code <<
       " Product Name: " << p.name << " Product Price: " << p.price << endl;
    //os << p.code << " " << p.name << " " << p.price << endl;
    return os;
}

Product &Product::operator=(const Product &p) {
    this->id_unic = p.id_unic;
    if(this != &p)
    {
        this->code = p.code;
        this->name = p.name;
        this->price = p.price;

    }
    else
        cout << "Error";
    return (*this);
}

bool Product::operator==(const Product &p) {
    return this->code == p.code && this->name == p.name && this->price == p.price;
}

Product::Product(int id, string _code, string _name, double _price) {
    id_aux = id;
    this->id_unic = id;
    this->code = _code;
    this->name = _name;
    this->price = _price;
}

void Product::Clear() {
    id_aux = 0;
}

Product::~Product() = default;

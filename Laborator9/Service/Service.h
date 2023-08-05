//
// Created by Sergiu on 26.04.2022.
//

#ifndef MAIN_CPP_SERVICE_H
#define MAIN_CPP_SERVICE_H


#include "../Repository/RepositoryInMemory.h"
#include "../Repository/RepositoryFile.h"
#include <map>
#include <cstring>
template<class T>
class Service {
private:
    RepositoryFile<T> repo;
public:
    Service();
    Service(const RepositoryFile<T>& _repo);
    void AddProduct(const T& p);
    void DeleteProduct(int id);
    void UpdateProduct(T oldp, T p);
    void BuyProduct(int id, double money, map<int, int>& myCoin, string tr);
    void RandomGenerate(int size, map<int, int>& myCoin, map<string, int>& myCount);
    T getProductId(int id);
    string RandomChoose(char s[]);
    bool CodeVerify(string code);
    bool NameVerify(string name);
    bool IdVerify(int id);
    vector<T> getAll();
    int getSize();


};
template<class T>
Service<T>::Service() {
    this->repo = RepositoryFile<T>();
}
template<class T>
Service<T>::Service(const RepositoryFile<T> &_repo) {
    this->repo = _repo;
}
template<class T>
void Service<T>::AddProduct(const T &p) {
    repo.AddEntity(p);
}
template<class T>
void Service<T>::DeleteProduct(int id) {
    repo.DeleteEntity(id);
}
template<class T>
vector<T> Service<T>::getAll() {
    return repo.getAll();
}
template<class T>
void Service<T>::BuyProduct(int id, double money, map<int, int>& myCoin, string tr) {
    Product p;
    bool G = false;
    for(auto& a: getAll())
        if(a.getIdUnic() == id)
        {
            p = a;
            G = true;
        }
    if(G) {
        double sum = 0;
        for (auto &c: myCoin)
            sum += c.first * c.second;
        sum /= 100;
        double rest = money - p.getPrice();
        double aux = rest;
        if (money >= p.getPrice()) {
            if (rest > sum) {
                if (tr != "test")
                    cout << "Candy Machine can't return the rest of money" << endl;
            } else {
                int index[5] = {0, 1, 5, 10, 50};
                int i = 4;
                rest *= 100;
                rest = (int) rest;
                rest = (double) rest;
                bool ok = true;
                while (rest - index[i] < 0) {
                    i--;
                }
                while (rest > 0 and ok) {
                    if (i > 0) {
                        if (myCoin[index[i]] != 0) {
                            if (rest - index[i] >= 0) {
                                rest -= index[i];
                                myCoin[index[i]]--;
                                if (myCoin[index[i]] == 0) {
                                    i--;
                                    if (i == 0)
                                        ok = false;
                                }
                            } else if (rest - index[i] < 0) {
                                i--;
                            }
                        } else
                            i--;
                    } else
                        ok = false;
                }
                if (rest == 0) {
                    if (tr != "test")
                        cout << "Your rest of money has returned succesfully" << endl;
                    DeleteProduct(id);
                    if (tr != "test")
                        cout << "Your rest of money: " << aux << endl;
                } else {
                    if (tr != "test")
                        cout << "Candy Machine can't return the rest of money" << endl;
                }
            }
        } else
            cout << "You don't have enough money" << endl;
    }
    else
        cout << "Product doesn't exist" << endl;
}
template<class T>
void Service<T>::RandomGenerate(int size, map<int, int>& myCoin, map<string, int>& myCount) {
    srand (time(NULL));
    char number[11] = {'1', '2', '3', '4', '5',
                       '6', '7', '8', '9', '0'};
    char character[27] = {'a', 'b', 'c', 'd', 'e',
                          'f', 'g', 'h', 'i', 'j',
                          'k', 'l', 'm', 'n', 'o',
                          'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'x', 'y', 'z'};
    myCount.clear();
    for(int i = 0; i < size; i++)
    {
        string code = RandomChoose(number);
        string name = RandomChoose(character);
        double price = rand() % 20 + 1;
        int count = rand() % 50 + 1;
        if(!CodeVerify(code) && !NameVerify(name) && price != 0)
        {
            Product p(code, name, price);
            myCount.emplace(code, count);
            AddProduct(p);
        }
    }
    int s[4] = {1, 5, 10, 50};
    int value;
    myCoin.clear();
    for(auto& i: s){
        value = rand() % 30 + 1;
        myCoin.emplace(i, value);
    }

}
template<class T>
string Service<T>::RandomChoose(char s[]) {
    string res = "";
    for(int i = 0; i < 4; i++)
    {
        int index = rand() % strlen(s);
        res += s[index];
    }
    return res;
}
template<class T>
bool Service<T>::CodeVerify(string code) {
    for(auto& a: getAll())
        if(a.getCode() == code)
            return true;
    return false;
}

template<class T>
T Service<T>::getProductId(int id) {
    for(auto& a: getAll())
        if(a.getIdUnic() == id)
            return a;
}

template<class T>
void Service<T>::UpdateProduct(T oldp, T p) {
    repo.UpdateEntity(oldp, p);
}

template<class T>
int Service<T>::getSize() {
    return repo.getSize();
}

template<class T>
bool Service<T>::IdVerify(int id) {
    for(auto& a: getAll())
        if(a.getIdUnic() == id)
            return true;
    return false;
}

template<class T>
bool Service<T>::NameVerify(string name) {
    for(auto& a: getAll())
        if(a.getName() == name)
            return true;
    return false;
}


#endif //MAIN_CPP_SERVICE_H

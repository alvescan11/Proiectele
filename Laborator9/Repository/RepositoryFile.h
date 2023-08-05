//
// Created by Sergiu on 26.04.2022.
//

#ifndef MAIN_CPP_REPOSITORYFILE_H
#define MAIN_CPP_REPOSITORYFILE_H
#include "RepositoryInMemory.h"
#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
#include <cstring>
#include <fstream>
template<class T>
class RepositoryFile: public RepositoryInMemory<T>{
private:
    char* fileName;
public:
    RepositoryFile();
    RepositoryFile(const char* fileName);
    ~RepositoryFile();
    void AddEntity(T p) override;
    void DeleteEntity(int id) override;
    void UpdateEntity(T oldp, T p) override;
    vector<T> getAll() override;
    void loadFromFile();
    void saveToFile();
};

template<class T>
RepositoryFile<T>::RepositoryFile() {
    this->fileName = NULL;
}

template<class T>
RepositoryFile<T>::RepositoryFile(const char *fileName) {
    //Product().id_aux = 0;
    if (fileName != NULL)
    {
        this->fileName = new char[strlen(fileName) + 1];
        strcpy_s(this->fileName, strlen(fileName) + 1, fileName);
    }
    else
    {
        this->fileName = NULL;
    }
    this->loadFromFile();
}

template<class T>
RepositoryFile<T>::~RepositoryFile() {
    if (fileName != NULL)
    {
        delete []this->fileName;
        this->fileName = NULL;
    }
}

template<class T>
void RepositoryFile<T>::loadFromFile() {
    if (this->fileName) {
        ifstream f(this->fileName);
        string Sid[2];
        string id;
        string code;
        string name;
        double price;
        while (!f.eof())
        {
            for (auto &i: Sid)
                f >> i;
            f >> id;
            for (auto &i: Sid)
                f >> i;
            f >> code;
            for (auto &i: Sid)
                f >> i;
            f >> name;
            for (auto &i: Sid)
                f >> i;
            f >> price;
            bool ok = false;
            for (auto &a: this->getAll())
                if (a.getCode() == code)
                    ok = true;
            int idd = 0;
            for(int j = 0; j < id.size(); j++)
                idd = idd * 10 + id[j] - '0';
            if(!ok) {
                Product p(idd, code, name, price);
                if (!(p == T())) {
                    this->AddEntity(p);
                }
            }
        }
        f.close();
    }
}

template<class T>
void RepositoryFile<T>::saveToFile() {
    if (this->fileName)
    {
        ofstream f(this->fileName);
        for(auto& a: this->getAll())
        {
            //cout << a;
            f << a;
        }
        f.close();
    }
}

template<class T>
void RepositoryFile<T>::AddEntity(T p) {
    RepositoryInMemory<T>::AddEntity(p);
    saveToFile();
}

template<class T>
void RepositoryFile<T>::DeleteEntity(int id) {
    RepositoryInMemory<T>::DeleteEntity(id);
    saveToFile();
}

template<class T>
void RepositoryFile<T>::UpdateEntity(T oldp, T p) {
    RepositoryInMemory<T>::UpdateEntity(oldp, p);
    saveToFile();
}

template<class T>
vector<T> RepositoryFile<T>::getAll() {
    return RepositoryInMemory<T>::getAll();
}



#endif //MAIN_CPP_REPOSITORYFILE_H

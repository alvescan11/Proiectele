//
// Created by Sergiu on 19.04.2022.
//

#ifndef MAIN_CPP_REPOSITORY_H
#define MAIN_CPP_REPOSITORY_H

#include <vector>
#include "../Domain/Product.h"
template<class T>
class Repository {
public:
    virtual void AddEntity(T p) = 0;
    virtual void DeleteEntity(int id) = 0;
    virtual void UpdateEntity(T oldp, T p) = 0;
    virtual vector<T> getAll() = 0;
};

#endif //MAIN_CPP_REPOSITORY_H

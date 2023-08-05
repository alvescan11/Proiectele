//
// Created by Sergiu on 19.04.2022.
//

#ifndef MAIN_CPP_REPOSITORYINMEMORY_H
#define MAIN_CPP_REPOSITORYINMEMORY_H

#include <vector>
#include "../Domain/Product.h"
#include "Repository.h"
template<class T>
class RepositoryInMemory: public Repository<T>{
private:
    vector<T> Entities;
public:
    RepositoryInMemory();
    RepositoryInMemory(const RepositoryInMemory& repo);
    virtual ~RepositoryInMemory();
    void AddEntity(T p) override;
    void DeleteEntity(int id) override;
    void UpdateEntity(T oldp, T p) override;
    RepositoryInMemory& operator=(const RepositoryInMemory& repo);
    vector<T> getAll() override;
    T& getEntity(int id);
    int getSize();

};

template<class T>
RepositoryInMemory<T>::RepositoryInMemory() {
    this->Entities = vector<T>();
}
template<class T>
RepositoryInMemory<T>::RepositoryInMemory(const RepositoryInMemory &repo) {
    this->Products = repo.Entities;
}
template<class T>
vector<T> RepositoryInMemory<T>::getAll() {
    return this->Entities;
}
template<class T>
RepositoryInMemory<T> &RepositoryInMemory<T>::operator=(const RepositoryInMemory &repo) {
    if(this != &repo)
    {
        this->Entities = repo.Entities;
    }
    else
        cout << "Error";
    return (*this);
}
template<class T>
int RepositoryInMemory<T>::getSize() {
    return this->Entities.size();
}
template<class T>
void RepositoryInMemory<T>::AddEntity(T p) {
    this->Entities.push_back(p);
}
template<class T>
void RepositoryInMemory<T>::DeleteEntity(int id) {
    vector<Product>::iterator aux;
    for(auto it = Entities.begin(); it < Entities.end(); it++)
        if(it->getIdUnic() == id)
            aux = it;
    this->Entities.erase(aux);
}
template<class T>
void RepositoryInMemory<T>::UpdateEntity(T oldp, T p) {
    Product newEntity(oldp.getIdUnic(), p.getCode(), p.getName(), p.getPrice());
    for(auto it = Entities.begin(); it < Entities.end(); it++)
        if(*it == oldp){
            *it = newEntity;
        }
}
template<class T>
T &RepositoryInMemory<T>::getEntity(int id) {
    for(T& e: Entities){
        if(e.getIdUnic() == id)
            return e;
    }
    throw runtime_error("No product with specified id found");
}
template<class T>
RepositoryInMemory<T>::~RepositoryInMemory() = default;

#endif //MAIN_CPP_REPOSITORYINMEMORY_H

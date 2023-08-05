//
// Created by Sergiu on 19.04.2022.
//

#include "Tests.h"
#include "../Repository/RepositoryFile.h"
#include "../Service/Service.h"

void TestProduct()
{
    Product p("123123123", "ciocolata", 123.3);
    assert(p.getCode() == "123123123");
    assert(p.getName() == "ciocolata");
    assert(p.getPrice() == 123.3);
    p.setCode("12312312");
    p.setName("ciocolat");
    p.setPrice(123.3);
    assert(p.getCode() == "12312312");
    assert(p.getName() == "ciocolat");
    assert(p.getPrice() == 123.3);
    p.Clear();
}
void AddEntityTest()
{
    RepositoryInMemory<Product> repo;
    assert(repo.getSize() == 0);
    Product p("123123", "ciocolata", 123.3);
    repo.AddEntity(p);
    assert(repo.getSize() == 1);
    p.Clear();

}
void DeleteEntityTest()
{
    RepositoryInMemory<Product> repo;
    Product p("123123", "ciocolata", 123.3);
    assert(repo.getSize() == 0);
    repo.AddEntity(p);
    assert(repo.getSize() == 1);
    repo.DeleteEntity(1);
    assert(repo.getSize() == 0);
    p.Clear();
}
void UpdateEntityTest()
{
    RepositoryInMemory<Product> repo;
    assert(repo.getSize() == 0);
    Product p("123123", "ciocolata", 123.3);
    repo.AddEntity(p);
    Product p1("1", "c", 123.3);
    repo.UpdateEntity(p, p1);
    assert(repo.getAll()[0].getCode() == "1");
    assert(repo.getAll()[0].getName() == "c");
    assert(repo.getAll()[0].getPrice() == 123.3);
    p.Clear();
}

void AddEntityFileTest()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    RepositoryFile<Product> repo("product.txt");
    Product p("123123", "ciocolata", 123.3);
    repo.AddEntity(p);
    assert(repo.getSize() == 1);

}

void DeleteEntityFileTest()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    file.close();
    RepositoryFile<Product> repo("product.txt");
    Product p("123123", "ciocolata", 123.3);
    assert(repo.getSize() == 0);
    repo.AddEntity(p);
    assert(repo.getSize() == 1);
    repo.DeleteEntity(1);
    assert(repo.getSize() == 0);
}

void UpdateEntityFileTest()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    file.close();
    RepositoryFile<Product> repo("product.txt");
    assert(repo.getSize() == 0);
    Product p("123123", "ciocolata", 123.3);
    repo.AddEntity(p);
    Product p1("1", "c", 123.3);
    repo.UpdateEntity(p, p1);
    assert(repo.getAll()[0].getCode() == "1");
    assert(repo.getAll()[0].getName() == "c");
    assert(repo.getAll()[0].getPrice() == 123.3);
}
void AddEntityService()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    RepositoryFile<Product> repo("product.txt");
    Service<Product> service(repo);
    Product p("123123", "ciocolata", 123.3);
    service.AddProduct(p);
    assert(service.getSize() == 1);
}
void DeleteEntityService()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    RepositoryFile<Product> repo("product.txt");
    Service<Product> service(repo);
    Product p("123123", "ciocolata", 123.3);
    service.AddProduct(p);
    assert(service.getSize() == 1);
    service.DeleteProduct(p.getIdUnic());
    assert(service.getSize() == 0);
}
void UpdateEntityService()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    RepositoryFile<Product> repo("product.txt");
    Service<Product> service(repo);
    Product p("123123", "ciocolata", 123.3);
    service.AddProduct(p);
    Product p1("1", "c", 1);
    service.UpdateProduct(p, p1);
    assert(service.getAll()[0].getCode() == "1");
    assert(service.getAll()[0].getName() == "c");
    assert(service.getAll()[0].getPrice() == 1);
}

void BuyProductTest()
{
    remove("product.txt");
    fstream file;
    file.open("product.txt", ios::in);
    file.open("product.txt", ios::out);
    RepositoryFile<Product> repo("product.txt");
    Service<Product> service(repo);
    map<int, int> myCoin;
    myCoin.emplace(pair<int ,int >(1, 10));
    myCoin.emplace(pair<int ,int >(5, 10));
    myCoin.emplace(pair<int ,int >(10, 10));
    myCoin.emplace(pair<int ,int >(50, 10));
    Product p("123123", "ciocolata", 7.5);
    service.AddProduct(p);
    assert(service.getSize() == 1);
    service.BuyProduct(p.getIdUnic(), 10, myCoin, "test");
    assert(service.getSize() == 0);

}
void TestAll()
{
    TestProduct();
    AddEntityTest();
    DeleteEntityTest();
    UpdateEntityTest();
    AddEntityFileTest();
    DeleteEntityFileTest();
    UpdateEntityFileTest();
    AddEntityService();
    DeleteEntityService();
    UpdateEntityService();
    BuyProductTest();
}
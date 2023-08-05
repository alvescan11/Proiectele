cmake_minimum_required(VERSION 3.21)
project(Laborator9)

set(CMAKE_CXX_STANDARD 14)

add_executable(Laborator9 main.cpp Domain/Product.cpp Domain/Product.h Repository/RepositoryInMemory.h Repository/Repository.h Tests/Tests.cpp Tests/Tests.h Repository/RepositoryFile.h Service/Service.h UserInterface/UserInterface.cpp UserInterface/UserInterface.h)

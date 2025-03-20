cmake_minimum_required(VERSION 3.10)

project(HelloWorld)

add_subdirectory(extern\\pybind11-2.13.6\\pybind11-2.13.6\\)
pybind11_add_module(target_del target_del_vlaue.cpp)

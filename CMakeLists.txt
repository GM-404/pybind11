cmake_minimum_required(VERSION 3.10)

project(HelloWorld)

add_subdirectory(extern/pybind11-2.13.6/pybind11-2.13.6/)

pybind11_add_module(example example.cpp)
pybind11_add_module(bind_class bind_class.cpp)
pybind11_add_module(tar_del tar_del.cpp)
pybind11_add_module(tar_cre tar_cre.cpp)
pybind11_add_module(tar_mov tar_mov.cpp)
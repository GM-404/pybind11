#include <pybind11/pybind11.h>
#include <iostream>
using namespace std;

void add(int i, int j)
{
    std::cout << "add" << i + j << std::endl;
}

PYBIND11_MODULE(target_del, m)
{
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &add, "A function which adds two numbers");
}
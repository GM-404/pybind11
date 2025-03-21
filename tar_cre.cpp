
#include <pybind11/pybind11.h>
#include <iostream>
#include <cstdint>

class Measurement
{
public:
    double speed;
    Measurement(double speed)
        : speed(speed) {}
};
int creat_targets(Measurement &measurements)
{
    float speed_threshold = 0.1; // 速度阈值  太慢的速度不要
    int uuid = 0;
    // 检查测量值的速度是否超过阈值
    if (std::abs(measurements.speed) > speed_threshold)
    {
        uuid++;
    }
    return uuid;
};

PYBIND11_MODULE(tar_cre, m)
{
    m.doc() = "pybind11 example plugin";
    pybind11::class_<Measurement>(m, "Measurement")
        .def(pybind11::init<float>())
        .def_readwrite("speed", &Measurement::speed);
    m.def("creat_targets", &creat_targets, "A function which creates targets");
}
#include <pybind11/pybind11.h>
#include <iostream>
#include <cstdint>

class TrackedTarget
{
public:
    int32_t uuid;
    int32_t target_score;
    TrackedTarget(int32_t uuid, int32_t target_score)
        : uuid(uuid),
          target_score(target_score) {}
};

int move_confirmed_targets(TrackedTarget &tracked_targets)
{
    if (tracked_targets.target_score >= 3000)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

PYBIND11_MODULE(tar_mov, m)
{
    m.doc() = "pybind11 example plugin";
    pybind11::class_<TrackedTarget>(m, "TrackedTarget")
        .def(pybind11::init<int32_t, int32_t>())
        .def_readwrite("uuid", &TrackedTarget::uuid)
        .def_readwrite("target_score", &TrackedTarget::target_score);
    m.def("move_confirmed_targets", &move_confirmed_targets, "A function whichmove_confirmed_targets");
}
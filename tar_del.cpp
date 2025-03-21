#include <pybind11/pybind11.h>
#include <iostream>
#include <cstdint>

class TrackedTarget
{
public:
    int32_t uuid;
    int32_t life_cycle;
    TrackedTarget(int32_t uuid, int32_t life_cycle)
        : uuid(uuid),
          life_cycle(life_cycle) {}
};

void delete_invalid_targets(TrackedTarget &a)
{
    if (a.life_cycle <= 0)
    {
        std::cout << "Target with UUID " << a.uuid << " is invalid and will be removed." << std::endl;
    }
};

PYBIND11_MODULE(tar_del, m)
{
    m.doc() = "pybind11 example plugin";
    pybind11::class_<TrackedTarget>(m, "TrackedTarget")
        .def(pybind11::init<int32_t, int32_t>())
        .def_readwrite("uuid", &TrackedTarget::uuid)
        .def_readwrite("life_cycle", &TrackedTarget::life_cycle);
    m.def("delete_invalid_targets", &delete_invalid_targets, "A function which deletes invalid targets");
}

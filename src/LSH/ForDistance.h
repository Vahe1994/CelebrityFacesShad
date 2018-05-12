#include <vector>
#include <string>


struct ForDistance {
    ForDistance(std::vector<float> elem_embedding, std::string elem_name, float distance)
            : embedding{elem_embedding}, name{elem_name}, distance{distance} {}
    std::vector<float> embedding;
    std::string name;
    float distance;
};
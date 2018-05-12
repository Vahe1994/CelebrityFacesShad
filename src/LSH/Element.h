#pragma once
#include <vector>
#include <string>


struct Element {
    Element(std::vector<float> elem_embedding, std::string elem_name)
            : embedding{elem_embedding}, name{elem_name} {}
    std::vector<float> embedding;
    std::string name;
};
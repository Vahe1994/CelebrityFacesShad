#include "LSH.h"
#include <iostream>
#include <algorithm>
#include <utility>


static bool PointsCompare(const ForDistance &first, const ForDistance &second) {
    return first.distance < second.distance;
}

std::string Hash(Plain& current_plain, std::vector<float>& point) {
    std::string result_string;
    std::vector<float> current_float_hash = current_plain * point;
    for (const auto& float_number : current_float_hash) {
        float_number > 0 ? result_string += '1' : result_string += '0';
    }
    return result_string;
}

float L2(std::vector<float>& left, std::vector<float>& right) {
    float result = 0.0;
    for (int i = 0; i < left.size(); ++i) {
        result += std::pow(left[i] - right[i], 2.0);
    }
    return result;
}

LSH::LSH(int bits_number, int embedding_dimention, int hashtable_number) {
    std::random_device rd;
    std::mt19937 generator{rd()};
    _bits_number = bits_number;
    _embedding_dimention = embedding_dimention;
    _hashtable_number = hashtable_number;
    for (int i = 0; i < _hashtable_number; ++i) {
        _storages.emplace_back(Storage());
        _plains.emplace_back(Plain(_bits_number, _embedding_dimention, generator));
    }
}

void LSH::AddToStorages(std::vector<float> point, const std::string &name) {
    for (int hash_table_i = 0; hash_table_i < _hashtable_number; ++hash_table_i) {
        _storages[hash_table_i].AppendValue(Hash(_plains[hash_table_i], point), point, name);
    }
}

std::vector<Element> LSH::FindNSimilar(std::vector<float> point, int number_of_similars) {
    std::vector<Element> similars;
    for (int hash_i = 0; hash_i < _hashtable_number; ++hash_i) {
        std::string point_hash = Hash(_plains[hash_i], point);
        std::vector<Element> current_elements = _storages[hash_i].GetValues(point_hash);
        while (!current_elements.empty()) {
            similars.push_back(current_elements[current_elements.size() - 1]);
            current_elements.pop_back();
        }
    }
    std::cout<< similars.size() << "\n";
    std::vector<ForDistance> point_distances;
    while (!similars.empty()) {
        point_distances.emplace_back(similars.back().embedding,
                                        similars.back().name,
                                        L2(similars.back().embedding, point));
        similars.pop_back();
    }
    std::sort(point_distances.begin(), point_distances.end(), PointsCompare);
    std::vector<Element> result;
    for (int i = 0; i < std::min<int>(number_of_similars, point_distances.size()); ++i) {
        result.emplace_back(point_distances[i].embedding, point_distances[i].name);
    }
    return result;
}

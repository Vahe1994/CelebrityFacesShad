#include <iostream>
#include <algorithm>
#include <random>
#include <vector>

#include "LSH.h"


std::string random_string( size_t length ) {
    auto randchar = []() -> char
    {
        const char charset[] =
                "0123456789"
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        "abcdefghijklmnopqrstuvwxyz";
        const size_t max_index = (sizeof(charset) - 1);
        return charset[ rand() % max_index ];
    };
    std::string str(length,0);
    std::generate_n( str.begin(), length, randchar );
    return str;
}

std::vector<float> random_float_vector(size_t length, std::mt19937& generator) {
    std::vector<float> result;
    std::normal_distribution<float> distribution(0.0, 1.0);
    float current_push = 0.0;
    for (int i = 0; i < length; ++i) {
        current_push = distribution(generator);
        result.push_back(current_push);
    }
    return result;
}

static float L1(std::vector<float>& left, std::vector<float>& right) {
    float result = 0.0;
    for (int i = 0; i < left.size(); ++i) {
        result += std::abs(left[i] - right[i]);
    }
    return result;
}

template <typename T>
const void PrintResults(std::vector<float>& point, std::vector<T>& elements) {
    std::cout << "Point\n";
    for (float k : point) {
        std::cout << k << " ";
    }
    std::cout << "\n";
    for (int i = 0; i < elements.size(); ++i) {
        std::cout << elements[i].name << ":\n";
        for (int j = 0; j < elements[i].embedding.size(); ++j) {
            std::cout << elements[i].embedding[j] << " ";
        }
        std::cout << "\n";
    }
}

int main() {
    std::random_device rd;
    std::mt19937 generator{rd()};
    LSH h = LSH(15, 20, 5);
    for (int i = 0; i < 100000; ++i) {
        h.AddToStorages(random_float_vector(128, generator), random_string(30));
    }
    auto point = random_float_vector(128, generator);
    auto res = h.FindNSimilar(point, 3);
    PrintResults(point, res);
    return 0;
}
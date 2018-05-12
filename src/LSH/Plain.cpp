#include "Plain.h"


Plain::Plain(int hight, int width, std::mt19937& g) : _bits_n{hight}, _emb_dim{width} {
    std::normal_distribution<float> distribution(0.0, 1.0);
    for (int i = 0; i < _bits_n; ++i) {
        std::vector<float> current_vector;
        for (int j = 0; j < _emb_dim; ++j) {
            float current_push = distribution(g);
            current_vector.push_back(current_push);
        }
        _plain.push_back(current_vector);
    }
}

std::vector<float> Plain::operator*(std::vector<float>& point) {
    std::vector<float> result((unsigned long) _bits_n, 0.0);
    for (int bits = 0; bits < _bits_n; ++bits) {
        for (int dim = 0; dim < _emb_dim; ++dim) {
            result[bits] += _plain[bits][dim] * point[dim];
        }
    }
    return result;
}
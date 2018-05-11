#include <random>
#include <vector>


struct Plain {
private:
    std::vector<std::vector<float>> _plain;
    int _bits_n;
    int _emb_dim;
public:
    Plain(int hight, int width, std::mt19937& g);
    std::vector<float> operator*(std::vector<float>& point);
};

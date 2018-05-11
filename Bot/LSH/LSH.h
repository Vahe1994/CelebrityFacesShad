
#include <vector>
#include <string>

#include "Element.h"
#include "Plain.h"
#include "Storage.h"
#include "ForDistance.h"


static bool PointsCompare(const ForDistance &first, const ForDistance &second);

std::string Hash(Plain& current_plain, std::vector<float>& point);

float L2(std::vector<float>& left, std::vector<float>& right);

class LSH {
private:
    int _bits_number;
    int _embedding_dimention;
    int _hashtable_number;
    std::vector<Storage> _storages;
    std::vector<Plain> _plains;
public:
    LSH(int bits_number, int embedding_dimention, int hashtable_number);
    void AddToStorages(std::vector<float> point, const std::string &name);
    std::vector<Element> FindNSimilar(std::vector<float> point, int number_of_similars);
};

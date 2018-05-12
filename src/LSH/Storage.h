#include <unordered_map>
#include <string>
#include <vector>
#include "Element.h"


class Storage {
private:
    std::unordered_map<std::string, std::vector<Element>> _storage;
public:
    void AppendValue(std::string key, const std::vector<float> &embedding_value, const std::string &name_value);
    std::vector<Element> GetValues(std::string& key);
};
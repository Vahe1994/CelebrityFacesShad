#include "Storage.h"


void Storage::AppendValue(std::string key, const std::vector<float> &embedding_value, const std::string &name_value) {
    if (_storage.find(key) == _storage.end()) {
        Element element_for_vector = Element({embedding_value, name_value});
        std::vector<Element> vector_for_value = std::vector<Element>({element_for_vector});
        std::pair<std::string, std::vector<Element>> pair_for_insert = std::make_pair<std::string,
                std::vector<Element>>((std::string &&) key, static_cast<std::vector<Element> &&>(vector_for_value));
        _storage.insert(pair_for_insert);
    } else {
        _storage[key].push_back(Element({embedding_value, name_value}));
    }
}

std::vector<Element> Storage::GetValues(std::string& key) {
    if (_storage.find(key) == _storage.end()) {
        return std::vector<Element>();
    }
    return _storage[key];
}
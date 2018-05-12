import cLSH


class LSH():
    def __init__(self, bits_number, embedding_dimention, hashtable_number):
        self.lshCapsule = cLSH.construct(bits_number, embedding_dimention, hashtable_number)

    def AddToStorages(self, point, name):
        cLSH.AddToStorages(self.lshCapsule, point, name)

    def FindNSimilar(self, point, number_of_similars):
        return cLSH.FindNSimilar(self.lshCapsule, point, number_of_similars)

    def __delete__(self):
        cLSH.delete_object(self.lshCapsule)

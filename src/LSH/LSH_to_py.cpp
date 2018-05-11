#include <Python.h>
#include <iostream>
#include "LSH.h"


PyObject* construct(PyObject* self, PyObject* args)
{
    int bits_number, embedding_dimention, hashtable_number;

    if (!PyArg_ParseTuple(args, "iii", &bits_number, &embedding_dimention, &hashtable_number)) {
        return NULL;
    }
    LSH* lsh = new LSH(bits_number, embedding_dimention, hashtable_number);

    PyObject* lshCapsule = PyCapsule_New((void *)lsh, "LSHptr", NULL);
    PyCapsule_SetPointer(lshCapsule, (void *)lsh);

    return Py_BuildValue("O", lshCapsule);
}

PyObject* AddToStorages(PyObject* self, PyObject* args)
{
    // Arguments passed from Python
    PyObject* lshCapsule_;
    PyObject* point;
    char* name;

    if (!PyArg_ParseTuple(args, "OO!s", &lshCapsule_, &PyList_Type, &point, &name)){
        return NULL;
    }

    std::vector<float> data;
    for(Py_ssize_t i = 0; i < PyList_Size(point); i++) {
			PyObject* x = PyList_GetItem(point, i);
			data.push_back(PyFloat_AsDouble(x));
	}
    LSH* lsh = (LSH*)PyCapsule_GetPointer(lshCapsule_, "LSHptr");
    lsh->AddToStorages(data, std::string(name));
    return Py_BuildValue("");
}

PyObject* FindNSimilar(PyObject* self, PyObject* args)
{
    // Arguments passed from Python
    PyObject* lshCapsule_;
    PyObject* point;
    int number_of_similars;

    if (!PyArg_ParseTuple(args, "OO!i", &lshCapsule_, &PyList_Type, &point, &number_of_similars)){
        return NULL;
    }

    std::vector<float> data;
    for(Py_ssize_t i = 0; i < PyList_Size(point); i++) {
			PyObject* x = PyList_GetItem(point, i);
			data.push_back(PyFloat_AsDouble(x));
	}

    LSH* lsh = (LSH*)PyCapsule_GetPointer(lshCapsule_, "LSHptr");
    std::vector<Element> elements = lsh->FindNSimilar(data, number_of_similars);

    PyObject* py_elements = PyList_New(elements.size());
    for (int i = 0; i < PyList_Size(py_elements); i++) {
        PyObject* embedding = PyList_New(elements[i].embedding.size());
        for (int j = 0; j < PyList_Size(embedding); j++) {
            PyObject* value = PyFloat_FromDouble((double)elements[i].embedding[j]);
            PyList_SET_ITEM(embedding, j, value);
        }
        PyObject* name = PyUnicode_FromString(elements[i].name.c_str());     
        PyObject* element = PyTuple_Pack(2, embedding, name);
        PyList_SET_ITEM(py_elements, i, element);
    }
    return py_elements;
}

PyObject* delete_object(PyObject* self, PyObject* args)
{
    PyObject* lshCapsule_;
    PyArg_ParseTuple(args, "O", &lshCapsule_);
    LSH* lsh = (LSH*)PyCapsule_GetPointer(lshCapsule_, "LSHptr");
    delete lsh;
    return Py_BuildValue("");
}

PyMethodDef cLSHFunctions[] =
{
    {"construct",
      construct, METH_VARARGS,
     "Create `LSH` object"},

    {"AddToStorages",
      AddToStorages, METH_VARARGS,
     "Add vector to storage"},

    {"FindNSimilar",
      FindNSimilar, METH_VARARGS,
     "Find similar vectors"},

    {"delete_object",
      delete_object, METH_VARARGS,
     "Delete `LSH` object"},

    {NULL, NULL, 0, NULL}
};


struct PyModuleDef cLSHModule =
{
   PyModuleDef_HEAD_INIT,
   "cLSH",
   NULL,
   -1,
   cLSHFunctions
};


PyMODINIT_FUNC PyInit_cLSH(void)
{
    return PyModule_Create(&cLSHModule);
}

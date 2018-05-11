CPYTHON3 = python3
CPP = g++

# C++ example
HEADERS = LSH.h Element.h ForDistance.h Plain.h Storage.h 
OBJECTS = LSH.o Element.o ForDistance.o Plain.o Storage.o use_lsh.o 
CPPNAME = use_lsh

# Python module
MODULE_SOURCE = LSH.cpp Element.cpp ForDistance.cpp Plain.cpp Storage.cpp LSH_to_py.cpp
MODULE_COMPILE_SCRIPT = compile_LSH_py_module.py

%.o: %.cpp $(HEADERS)
		$(CPP) -c $<

# Build C++ application of `LSH` class.
use_lsh_cpp: $(OBJECTS)
	$(CPP) -o $(CPPNAME) $(OBJECTS)

# Build Python `LSH` module
lsh_py_module: $(MODULE_SOURCE) $(MODULE_COMPILE_SCRIPT) $(HEADERS)
	$(CPYTHON3) $(MODULE_COMPILE_SCRIPT) build_ext --inplace

# Clean up the current directory
.PHONY: clean
clean:
	rm -fR build
	rm -f *.so
	rm -f *.o
	rm -fR __pycache__
	rm -f use_lsh


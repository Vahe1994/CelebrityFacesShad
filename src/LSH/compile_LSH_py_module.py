from distutils.core import setup, Extension


cLSH = Extension('cLSH',
                 sources = ['LSH.cpp', 'LSH_to_py.cpp', 
                            'Element.cpp', 'ForDistance.cpp',
                            'Plain.cpp', 'Storage.cpp'])

# Compile Python module
setup (ext_modules = [cLSH],
       name = 'cLSH',
       description = 'cLSH Python module',
       version = '1.0')

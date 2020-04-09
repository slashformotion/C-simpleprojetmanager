# Cppsimpleprojetmanager

A simple python script to create and manage simple c++ projects.
With it you can create a main.cpp file and modules with or without namespaces and with or without class declarations. You can also create new modules and automatically integrate them to your code.

## Prerequisites

- Python 3.6 or newer

## Install

```git clone https://github.com/slashformotion/cppsimpleprojetmanager.git```   or download the zip archive

Then you can compile it if you want (check [this](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/235020-distribuer-facilement-nos-programmes-python-avec-cx-freeze)) or you can just use it the classic way with :

 ```python(x) <path/to/cppsimpleprojetmanager.py>```

 Personally I use this alias to make is usable in all my system :
 ```alias cppmanager='python3 <path/to/cppsimpleprojetmanager.py>'```

 ## Juste use it ! (but this not so straightforward)

 The syntax is simple :
 ```cppmanager mode main_file_name module1::namespace1::class1 module2::namespace2```
There is two modes :
- create
- add

### CREATE


exemple : ```cppmanager create prog mod1::namespace1::class1``` will generate 3 files :

(we can create any number of modules by adding the same syntax over and over ex:
     ```cppmanager create prog mod1::namespace1::class1 mod2::namespace2::class2 mod3::namespace3::class3```)

-------
prog.cpp
```
// File : prog.cpp
// Created : Thursday 09 April at 17h - 17min
// user : slash

//// PERSONAL MODULES
#include "mod1.hpp"

//// BUILTIN LIBS
#include <iostream>

int main(){

     return 0;
}
```
-------
mod1.hpp

```
#ifndef MOD1_NAMESPACE1_HPP
#define MOD1_NAMESPACE1_HPP

namespace namespace1
{
    class Class1
    {
        public:

        private:

    }; // class Class1
} // namespace namespace1

#endif // MOD1_NAMESPACE1_HPP
```
-------
mod1.cpp
```
#include "mod1.hpp"
namespace namespace1
{

} // namespace namespace1
```

### ADD

This mode integrate new modules into an existing project.
To use this mode, a main file is required (ex prog.cpp)
exemple : ```cppmanager add prog mod50::namespace50```

It will add an include directive in the prog.cpp : `#include "mode50.hpp"` and it will create the appropriate files `mod50.hpp` and `mod50.cpp`

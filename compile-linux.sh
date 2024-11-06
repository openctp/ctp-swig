#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: ./$0 <ctpapi version 1: 6.3.19> <ctpapi version 2: 6.6.7> ..."
  exit 1
fi


for arg in "$@"; do

    echo -e "\n######################################################## Enter $arg #######################\n"

    cd $arg

    echo -e "\n######################################################## Clear files #######################\n"

    rm -rf build
    rm *_wrap.*

    echo -e "\n################################################ Swig generate cpp/py files ################\n"

    mkdir -p py

    swig -threads -c++ -python -outdir py -outcurrentdir -Ilin64 ../thosttraderapi.i
    swig -threads -c++ -python -outdir py -outcurrentdir -Ilin64 ../thostmduserapi.i


    echo -e "\n######################################################### Compile ##########################\n"

    cp ../CMakeLists.txt .

    mkdir build
    mkdir py

    cmake -S. -B build
    cmake --build build --config Release --clean-first

    cp build/_thosttraderapi.so py/_thosttraderapi.so
    cp build/_thostmduserapi.so py/_thostmduserapi.so


    echo -e "\n####################################################### Clear files #######################\n"

    rm -rf build
    rm *_wrap.*
    rm CMakeLists.txt
    cd ..
done

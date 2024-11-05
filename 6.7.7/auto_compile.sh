#!/bin/bash

# 删除 build 目录和 *_wrap.* 文件
rm -rf build
rm *_wrap.*

echo "################## Swig generate cpp/py files ##################"
mkdir -p py
swig -threads -c++ -python -outdir py -outcurrentdir -Ilin64 ../thosttraderapi.i
swig -threads -c++ -python -outdir py -outcurrentdir -Ilin64 ../thostmduserapi.i

echo "########################## Compile ##########################"
mkdir build
mkdir py
cmake -S. -B build
cmake --build build --config Release --clean-first
cp build/_thosttraderapi.so py/_thosttraderapi.so
cp build/_thostmduserapi.so py/_thostmduserapi.so
rm -rf build
rm *_wrap.*

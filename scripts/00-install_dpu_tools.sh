#!/bin/bash

git clone git@github.com:upmem/dpu_tools.git
cd dpu_tools

git checkout 4a3e0b2d8bfe712a4628bc010e1de385617715c0 #version of SDK with timeout issue
git submodule update --init --recursive

mkdir build && cd build
cmake .. -G Ninja -DBUILD_DOCS=OFF
cmake --build .
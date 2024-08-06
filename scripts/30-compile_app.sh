#!/bin/bash

APP_DIR=../c_program

pushd $APP_DIR

make clean && make

popd
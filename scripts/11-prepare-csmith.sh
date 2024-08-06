#!/bin/bash

DPU_TOOLCHAIN_FILE="${BUILD_DIR}/build/dpu_toolchain.cfg"

pushd $BUILD_DIR

source upmem_env.sh

{
echo "test.CSMITH_INCLUDE_PATH=$(pwd)/../upmem_utilities/csmith/src/main/c/bsp"
echo "test.MULTI_DPU_TEST_ENABLED=true"
echo "test.ENABLE_PERF_TESTS_WITH_OUTPUT=true"
} > "${DPU_TOOLCHAIN_FILE}"

export DPU_TOOLCHAIN_CFG="${DPU_TOOLCHAIN_FILE}"

cmake .. -G Ninja -DDPU_TEST_TARGET=hw_dimms -DPython3_EXECUTABLE="$(which python3)" -DUSE_CCACHE=OFF

popd
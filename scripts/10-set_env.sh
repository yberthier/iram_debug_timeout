#!/bin/bash
export BUILD_DIR=$1

source_sdk(){
    source "${BUILD_DIR}/upmem_env.sh"
}

source_sdk

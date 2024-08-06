BUILD_DIR=~/dpu_tools/build
VERBOSITY=api:4,ufi:3

# source sdk
source ${BUILD_DIR}/upmem_env.sh
export UPMEM_VERBOSE="${VERBOSITY}"

gdb -x gdb-script.txt --args ./build/checksum_host

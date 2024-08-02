#!/bin/bash

# This script takes the dpu*.log file as argument and keep only dpu_launch and dpu_load
FILE_PATH=$1

cp "$FILE_PATH" "${FILE_PATH}.bak"
grep -E "dpu_load:|dpu_launch:" "${FILE_PATH}.bak" > "${FILE_PATH}.trimmed"

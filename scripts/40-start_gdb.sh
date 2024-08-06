#!/bin/bash

cd ../c_program

#inject breakpoint line number
line=$(grep -n 'in_progress = !determine_if_commands_are_finished' ${BUILD_DIR}/../backends/ufi/src/ufi_ci.c  | cut -d: -f1)
break_cmd="b ufi_ci.c : $line"
search_string="b ufi_ci.c"
replacement_string="b ufi_ci.c : $line if nr_retries <= 1"
sed -i "/${search_string}/c\\${replacement_string}" ../c_program/gdb-script.txt

#run gdb

gdb -x ../c_program/gdb-script.txt --args ../c_program/build/checksum_host

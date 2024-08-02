/*
 * Copyright (c) 2014-2019 - UPMEM
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @file host.c
 * @brief Template for a Host Application Source File.
 */

#include <dpu.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <dpu_management.h>


#ifndef DPU_BINARY
#define DPU_BINARY "afterSwResetIram7061056236090871404.iram"
#endif
/**
 * @brief Main of the Host Application.
 */
int main()
{
    struct dpu_set_t dpu_set, dpu;
    uint32_t nr_of_dpus;
    bool status = true;

    DPU_ASSERT(dpu_alloc(1, NULL, &dpu_set));

    DPU_ASSERT(dpu_get_nr_dpus(dpu_set, &nr_of_dpus));
    printf("Allocated %d DPU(s)\n", nr_of_dpus);

    DPU_FOREACH(dpu_set, dpu) {
        int i = 0;
        while(1){
            printf("%d\n", i++);
            DPU_ASSERT(dpu_load(dpu, DPU_BINARY, NULL));
        }
    }
    return status ? 0 : -1;
}

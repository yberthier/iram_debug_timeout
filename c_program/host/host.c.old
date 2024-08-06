
#include <dpu.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <dpu_management.h>


#ifndef DPU_BINARY
#define DPU_BINARY "build/checksum_dpu"
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
    printf("Allocated %d DPU(s)", nr_of_dpus);

    DPU_FOREACH(dpu_set, dpu) {
        while(1){
        dpu_load(dpu, DPU_BINARY, NULL);}
    }
    return status ? 0 : -1;
}


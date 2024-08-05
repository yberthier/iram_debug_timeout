#!/usr/bin/env python3


import re
import os
import sys
import argparse
      

class CodeGenerator:
    def __init__(self, path_to_log, path_to_source):
        try:
            self.f_source = open(path_to_source, 'w')
        except:
            print("Failed to open source file")
        
        try:
            self.f_log = open(path_to_log, 'r')
        except:
            print("Failed to open log file")

    def __del__(self):
        self.f_source.close()
        self.f_log.close()
    
    def write_dpu_load_cmd(self, path_to_binary: str):
        cmd = self.get_load_cmd(path_to_binary)
        self.f_source.write(cmd)

    def write_dpu_launch_cmd(self):
        cmd = self.get_launch_cmd()
        self.f_source.write(cmd)

    def parse_line(self, line):
        cmd_type = ""
        args = []
        if "dpu_load" in line:
            match = re.search(r'dpu_load: "([^"]+)"', line)
            if match:
                file_path = match.group(1)
                args.append(file_path)
                cmd_type = "load"
        if "dpu_launch:" in line:
            cmd_type = "launch"
            
        return cmd_type, args

    def generate(self):
        self.write_start()
        lines = self.f_log.readlines()
        for line in lines:
            cmd_type, args = self.parse_line(line)
            if cmd_type == "":
                continue
            elif cmd_type == "launch":
                self.write_dpu_launch_cmd()
            elif cmd_type == "load":
                self.write_dpu_load_cmd(args[0])
        self.write_end()

    def get_load_cmd(self, path_to_binary: str):
        raise NotImplementedError

    def get_launch_cmd(self):
        raise NotImplementedError

    def write_start(self):
        raise NotImplementedError

    def write_end(self):
        raise NotImplementedError

class CodeGeneratorJava(CodeGenerator):
    def get_load_cmd(self, path_to_binary: str):
        return f'system.load("{path_to_binary}");\n'

    def get_launch_cmd(self):
        return "system.exec();\n"

    def write_start(self):
        java_code = """
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import com.upmem.dpu.Dpu;
import com.upmem.dpu.DpuException;
import com.upmem.dpu.DpuSystem;

public class TrivialChecksumExampleMultiRank {

  public static void main(String[] args) throws DpuException {
    //try(DpuSystem system = DpuSystem.allocate(DpuSystem.ALLOCATE_ALL, "")) {
    try(DpuSystem system = DpuSystem.allocate(1, "")) {

      for (int i = 0; i < 10000000; i++){
        System.out.println(i);
"""
        self.f_source.write(java_code)
    
    def write_end(self):
        java_code = """
            }
        }
    }
}
"""
        self.f_source.write(java_code)

class CodeGeneratorC(CodeGenerator):
    def get_load_cmd(self, path_to_binary: str):
        return f'dpu_load(dpu, "{path_to_binary}", NULL);\n'

    def get_launch_cmd(self):
        return "dpu_launch(dpu);\n"

    def write_start(self):
        c_code = """
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
"""
        self.f_source.write(c_code)
    
    def write_end(self):
        c_code = """
    }
    return status ? 0 : -1;
}

"""
        self.f_source.write(c_code)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate code")
    parser.add_argument("dpu_log", type=str, help="Path to dpu-log.log file")
    parser.add_argument("generated_code", type=str, help="Path to generated code")
    parser.add_argument("language", type=str, help="Type of programming language")

    return parser.parse_args()



def main(arguments):
    args = parse_arguments()

    dpu_log_path = args.dpu_log
    path_code = args.generated_code
    language_type = args.language
    
    if(args.language == "java"):
        codeGen = CodeGeneratorJava(dpu_log_path, path_code)
    if(args.language == "C"):
        codeGen = CodeGeneratorC(dpu_log_path, path_code)
    codeGen.generate()
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

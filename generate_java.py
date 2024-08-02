#!/usr/bin/env python3


import re
import os
import sys
import argparse
      

class codeGenerator:
    def __init__(self, path_to_source, path_to_cmd):
        self.f_source = open(path_to_source, 'a+')
        self.f_cmd = open(path_to_cmd, 'r')
    def __del__(self):
        self.f_source.close()
        self.f_cmd.close()
        
    def write_dpu_load_cmd(self, path_to_binary: str):
        cmd = f'system.load("{path_to_binary}");\n'
        self.f_source.write(cmd)
    def write_dpu_launch_cmd(self):
        cmd = "system.exec();\n"
        self.f_source.write(cmd)
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

    
    def parse_line(self, line):
        #return type of command and args of the command
        cmd_type = ""
        args = []
        if "dpu_load" in line:
            match = re.search(r'dpu_load: "([^"]+)"', line)
            file_path = match.group(1)
            args.append(file_path)
            cmd_type = "load"
        if "dpu_launch:" in line:
            cmd_type = "launch"
            
        return cmd_type, args
        
    def generate(self):
        self.write_start()
        lines = self.f_cmd.readlines()
        for line in lines:
            cmd_type, args = self.parse_line(line)
            if(cmd_type == ""):
                continue
            elif(cmd_type == "launch"):
                self.write_dpu_launch_cmd()
            elif(cmd_type == "load"):
                self.write_dpu_load_cmd(args[0])
        self.write_end()


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to cmd file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="path to generated code",
                        default=sys.stdout, type=argparse.FileType('w'))
    args = parser.parse_args(arguments)

    codeGen = codeGenerator("out.java", "dpu.log")
    codeGen.generate()
    
    
    
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

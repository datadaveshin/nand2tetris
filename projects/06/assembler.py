#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Parser for the Hack Programming Assembler"""

import sys
from hackparser import Parser
from codetranslator import Code

def filename_valid(fname):
    """Checks if file extension is asm"""
    split_filename = fname.split('.')
    has_min_two_parts = len(split_filename) >= 2
    basename_has_min_one_char = len(split_filename[0]) >= 1
    ends_in_asm = split_filename[-1] == 'asm'
    return has_min_two_parts and basename_has_min_one_char and ends_in_asm

def filename_given(args_list):
    """Calculates whether an filename argument was given"""
    return len(args_list) >= 2

def main():
    """Translates assembly symbolic code to binary code"""

    if filename_given(sys.argv) and filename_valid(sys.argv[1]):
        input_filename = sys.argv[1]
        output_filename = f"{input_filename.split('.')[0]}.hack"

        try:
            infile = open(input_filename, "r")
        except FileNotFoundError:
            print("File not found")
        else:
            outfile = open(f"{output_filename}", "w")
            outfile = open(f"{output_filename}", "a")

            line_counter = 0
            line = infile.readline()

            while line:
                parser = Parser(line)
                parser.get_instruction()
                if parser.instruction_is_command():
                    parser.set_instruction_type()

                    if parser.instruction_type == "A_INSTRUCTION":
                        instruction = parser.get_a_symbol()
                        code = Code(instruction)
                        instruction = code.translate_a_or_l_instruction()
                        line_counter += 1

                    elif parser.instruction_type == "L_INSTRUCTION":
                        instruction = parser.get_l_symbol()
                        code = Code(instruction)
                        instruction = code.translate_a_or_l_instruction()

                    elif parser.instruction_type == "C_INSTRUCTION":
                        dest = parser.get_dest()
                        dest = Code(dest)
                        dest = dest.translate_dest()
                        jump = parser.get_jump()
                        jump = Code(jump)
                        jump = jump.translate_jump()
                        comp = parser.get_comp()
                        comp = Code(comp)
                        comp = comp.translate_comp()
                        instruction = code.concatenate_c_instruction(comp, dest, jump)
                        line_counter += 1

                    outfile.write(f"{instruction}\n")
                line = infile.readline()

            infile.close()
            outfile.close()
    else:
        print("Usage:\n./assembler.py <filename>.asm")

if __name__ == "__main__":
    main()

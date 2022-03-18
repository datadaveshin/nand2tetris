#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Parser for the Hack Programming Assembler"""

import sys
import codecs
from hackparser import Parser

def file_extension_is_asm(fname):
    """Checks if file extension is asm"""
    return fname.split('.')[-1] == 'asm'

def main():
    """Translates assembly symbolic code to binary code"""
    if sys.argv[1]:
        input_file = sys.argv[1]
        print(input_file)
    else:
        print("Usage: ./assembler.py <filename>.asm")

    if file_extension_is_asm(input_file):
        infile = codecs.open(input_file, "r", "utf-8-sig")
        outfile = codecs.open(f"{input_file.split('.')[0]}.hack", "w", "utf-8-sig")
        outfile = codecs.open(f"{input_file.split('.')[0]}.hack", "a", "utf-8-sig")

        line = infile.readline()
        while line:
            parser = Parser(line)
            parser.remove_leading_trailing_white_space()
            parser.extract_instruction()
            if parser.is_instruction_line(): # HERE REPLACE WITH A, C, L instruction
                # then here, do the coding logic 
                outfile.write(f"{parser.instruction}\n")
                print(parser.instruction)
            line = infile.readline()

        infile.close()
        outfile.close()
    else:
        print("File must have extension '.asm'")

if __name__ == "__main__":
    main()

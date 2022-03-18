#!/usr/bin/env python3
import sys
from parser_readlines import Parser

def file_extension_is_asm(fname):
    return fname.split('.')[-1] == 'asm'

def main():
    if sys.argv[1]:
        file = sys.argv[1]
        print(file)
    else:
        print("Usage: ./assembler.py <filename>.asm")

    if file_extension_is_asm(file):
        f = open(file, "r")
        instructions = f.readlines()
        parser = Parser(instructions)
        parser.remove_leading_trailing_white_space()
        parser.remove_empty_lines()
        parser.remove_comment_lines()
        parser.remove_inline_comments()
        print(parser)
    else:
        print(f"File must have extension '.asm'")

if __name__ == "__main__":
    main()

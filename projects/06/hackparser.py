#!/usr/bin/env python3
"""
Parses an array containing instructions for the Assembler
"""

class Parser():
    """docstring for Parser."""

    def __init__(self, instruction):
        self.instruction = instruction

    def __str__(self):
        return f"{self.instruction}"

    def remove_leading_trailing_white_space(self):
        """Strips white space from beginning and end of instruction"""
        self.instruction = self.instruction.strip(' \t\r\n')

    def is_instruction_line(self):
        """Checks if the line is an instruction"""
        return not (self.instruction == "" or self.instruction[0:2] == "//")

    def extract_instruction(self):
        """Extracts just the instruction, ie. removes comments from line"""
        self.instruction = self.instruction.split(' ')[0]

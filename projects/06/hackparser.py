#!/usr/bin/env python3
"""
Parses an array containing instructions for the Assembler
"""

class Parser():
    """docstring for Parser."""

    def __init__(self, instruction):
        self.instruction = instruction
        self.instruction_type = None

    def __str__(self):
        return f"{self.instruction}"

    def remove_leading_trailing_white_space(self):
        """Strips white space from beginning and end of instruction"""
        self.instruction = self.instruction.strip(' \t\r\n')

    def instruction_is_command(self):
        """Checks if the line is an instruction"""
        return not (self.instruction == "" or self.instruction[0] == "/")

    def get_instruction(self):
        """Extracts just the instruction, ie. removes comments from line"""
        self.remove_leading_trailing_white_space()
        self.instruction = self.instruction.split(' ')[0]

    def set_instruction_type(self):
        """Sets the type of instruction within the Parser object"""
        if self.instruction[0] == "@":
            self.instruction_type = "A_INSTRUCTION"
        elif self.instruction[0] == "(":
            self.instruction_type = "L_INSTRUCTION"
        else:
            self.instruction_type = "C_INSTRUCTION"

    def get_a_symbol(self):
        """Removes the '@' from A instructions"""
        return self.instruction[1:]

    def get_l_symbol(self):
        """Removes parentheses from Label instructions"""
        return self.instruction[1:-1]

    def get_dest(self):
        """Returns the dest part of the command"""
        if "=" in self.instruction:
            return self.instruction.split("=")[0]
        return ""

    def get_comp(self):
        """Returns the comp part of the command"""
        if "=" in self.instruction:
            return self.instruction.split("=")[1]
        if ";" in self.instruction:
            return self.instruction.split(";")[0]
        return ""

    def get_jump(self):
        """Returns the jump part of the command"""
        if ";" in self.instruction:
            return self.instruction.split(";")[-1]
        return ""

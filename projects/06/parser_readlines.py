#!/usr/bin/env python3
"""
Parses an array containing instructions for the Assembler
"""

class Parser():
    """docstring for Parser."""

    def __init__(self, instructions):
        self.instructions = instructions

    def __str__(self):
        ret_str = ""
        for instruction in self.instructions:
            ret_str += f"{instruction}\n"
        return ret_str

    def remove_leading_trailing_white_space(self):
        self.instructions = [instruction.strip(' \t\r\n') for instruction in self.instructions]

    def is_empty_line(line):
        if line == "":
            return False
        else:
            return True

    def remove_comment_lines(self):
        filtered = filter(lambda instruction: instruction[0:2] != "//", self.instructions)
        self.instructions = [item for item in filtered]

    def remove_empty_lines(self):
        filtered = filter(lambda instruction: instruction != "", self.instructions)
        self.instructions = [item for item in filtered]

    def remove_inline_comments(self):
        mapped = map(lambda instruction: instruction.split(' ')[0], self.instructions)
        self.instructions = [item for item in mapped]

    def hello_world(self):
        print("hello_world")

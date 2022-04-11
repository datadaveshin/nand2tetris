#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Translates symbolic code to binary code"""
from tables import DEST_TABLE, JUMP_TABLE, COMP_TABLE

BITS = 16

class Code():
    """docstring for Code Translator."""

    def __init__(self, instruction):
        self.instruction = instruction
        self.dest = DEST_TABLE
        self.jump = JUMP_TABLE
        self.comp = COMP_TABLE

    def decimal2binary(self, decimal, binary_code=""):
        """Recursive method to translate decimal to binarycode"""
        decimal = int(decimal)
        modulo = decimal % 2
        quotient = decimal // 2
        binary_code = str(modulo) + binary_code
        if quotient >= 1:
            return self.decimal2binary(quotient, binary_code)
        return binary_code

    def pad_binary(self, binary_code):
        """Pads binary code with leading zeros"""
        return (BITS - len(binary_code)) * "0" + binary_code

    def translate_a_or_l_instruction(self):
        """Translates A or L symbolic instructions to binary"""
        return self.pad_binary(self.decimal2binary(self.instruction))

    def translate_dest(self):
        """Translates 'destination' portion of a C-instruction to binary"""
        if self.instruction:
            return self.dest[self.instruction]
        return "000"

    def translate_comp(self):
        """Translates 'computation' portion of a C-instruction to binary"""
        if self.instruction:
            return self.comp[self.instruction]
        return "000000"

    def translate_jump(self):
        """Translates 'jump' address of a C-instruction to binary"""
        if self.instruction:
            return self.jump[self.instruction]
        return "000"

    def concatenate_c_instruction(self, comp, dest, jump):
        """Concatenates the comp, dest, jump instructions"""
        return f"111{comp}{dest}{jump}"
